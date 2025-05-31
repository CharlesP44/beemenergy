import aiohttp
from datetime import timedelta
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

BEEM_API_BASE = "https://api-x.beem.energy/beemapp"


class BeemCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, token: str, battery_id: int, email: str, password: str):
        """Initialise le coordinateur Beem."""
        self.token = token
        self.battery_id = battery_id
        self.email = email
        self.password = password

        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{battery_id}",
            update_interval=timedelta(seconds=60),
        )

    async def _async_update_data(self):
        """Récupère les données de la batterie depuis l'API Beem."""
        url = f"{BEEM_API_BASE}/batteries/{self.battery_id}/live-data"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 401:
                        _LOGGER.warning("Token expiré, tentative de renouvellement...")
                        if await self._refresh_token():
                            headers["Authorization"] = f"Bearer {self.token}"
                            async with session.get(url, headers=headers) as retry_response:
                                if retry_response.status == 200:
                                    return await retry_response.json()
                                raise UpdateFailed(f"Erreur après renouvellement du token: {retry_response.status}")
                        else:
                            raise UpdateFailed("Échec du renouvellement du token")

                    if response.status != 200:
                        text = await response.text()
                        raise UpdateFailed(f"Erreur API Beem ({response.status}): {text}")

                    return await response.json()

        except Exception as e:
            _LOGGER.exception("Erreur lors de la récupération des données: %s", e)
            raise UpdateFailed(f"Exception API Beem: {e}")

    async def _refresh_token(self) -> bool:
        """Renouvelle le token en cas d'expiration."""
        login_url = f"{BEEM_API_BASE}/user/login"
        payload = {
            "email": self.email,
            "password": self.password
        }
        headers = {"Content-Type": "application/json"}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(login_url, json=payload, headers=headers) as resp:
                    if resp.status != 200:
                        _LOGGER.error("Échec de la reconnexion Beem (%s)", resp.status)
                        return False
                    json_data = await resp.json()
                    self.token = json_data.get("accessToken")
                    _LOGGER.info("Nouveau token Beem obtenu avec succès")
                    return True
        except Exception as e:
            _LOGGER.exception("Erreur lors du renouvellement du token: %s", e)
            return False
