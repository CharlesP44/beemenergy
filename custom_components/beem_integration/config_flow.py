from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN
import aiohttp
import json as json_lib
import logging

_LOGGER = logging.getLogger(__name__)

class BeemConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            email = user_input["email"]
            password = user_input["password"]

            token, battery_id = await self._get_token_and_id(email, password)
            if token and battery_id:
                return self.async_create_entry(
                    title=email,
                    data={
                        "email": email,
                        "password": password,  # ❗ Attention : en clair ici
                        "token": token,
                        "battery_id": battery_id
                    }
                )
            else:
                errors["base"] = "auth_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("email"): str,
                vol.Required("password"): str
            }),
            errors=errors
        )

    async def _get_token_and_id(self, email, password):
        url_login = "https://api-x.beem.energy/beemapp/user/login"
        url_batteries = "https://api-x.beem.energy/beemapp/batteries/"
        headers = {"Content-Type": "application/json"}
        payload = {"email": email, "password": password}
        payload_raw = json_lib.dumps(payload)

        timeout = aiohttp.ClientTimeout(total=10)

        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url_login, data=payload_raw, headers=headers) as resp:
                    response_text = await resp.text()
                    if resp.status not in (200, 201):
                        _LOGGER.error("Échec de l'authentification Beem (%s): %s", resp.status, response_text)
                        return None, None
                    json_data = await resp.json()
                    token = json_data.get("accessToken")

                if token:
                    headers["Authorization"] = f"Bearer {token}"
                    async with session.get(url_batteries, headers=headers) as resp:
                        if resp.status != 200:
                            _LOGGER.error("Échec lors de la récupération des batteries (%s)", resp.status)
                            return token, None
                        json_data = await resp.json()
                        batteries = json_data.get("batteries")
                        if isinstance(batteries, list) and batteries:
                            battery_id = batteries[0].get("id")
                        else:
                            _LOGGER.error("Format inattendu ou vide des batteries: %s", json_data)
                            battery_id = None

                        return token, battery_id

        except Exception as e:
            _LOGGER.exception("Erreur inattendue lors de la récupération du token et ID: %s", e)
            return None, None
