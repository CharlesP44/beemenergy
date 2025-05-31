"""Beem Integration - Init file."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import BeemCoordinator

PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Beem Integration from a config entry."""

    # Initialise le domaine si nécessaire
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    # Empêche le double chargement
    if entry.entry_id in hass.data[DOMAIN]:
        return False

    # Crée le coordinateur
    coordinator = BeemCoordinator(
        hass=hass,
        token=entry.data["token"],
        battery_id=entry.data["battery_id"],
        email=entry.data["email"],
        password=entry.data.get("password"),  # Utilisé pour le renouvellement si besoin
    )
    await coordinator.async_config_entry_first_refresh()

    # Stocke le coordinator directement
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Utilise la nouvelle API (non-dépréciée) avec await
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
