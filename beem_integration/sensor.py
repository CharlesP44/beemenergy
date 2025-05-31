from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN

SENSOR_DEFINITIONS = {
    "batteryPower": "W",
    "meterPower": "W",
    "solarPower": "W",
    "activePower": "W",
    "soc": "%",
    "workingModeLabel": None,
    "lastKnownMeasureDate": None,
    "numberOfCycles": None,
    "numberOfModules": None,
    "globalSoh": "%",
    "capacityInKwh": "kWh",
    "maxPower": "W",
    "isBatteryWorkingModeOk": None
}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    battery_id = entry.data["battery_id"]

    sensors = [
        BeemSensor(coordinator, sensor_key, battery_id, unit)
        for sensor_key, unit in SENSOR_DEFINITIONS.items()
    ]
    async_add_entities(sensors)

class BeemSensor(SensorEntity):
    def __init__(self, coordinator, sensor_key, battery_id, unit):
        self.coordinator = coordinator
        self._sensor_key = sensor_key
        self._battery_id = battery_id

        self._attr_unique_id = f"{battery_id}_{sensor_key}"
        self._attr_name = sensor_key
        self._attr_native_unit_of_measurement = unit
        self._attr_has_entity_name = True

    @property
    def available(self):
        return self.coordinator.last_update_success

    @property
    def native_value(self):
        return self.coordinator.data.get(self._sensor_key)

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, str(self._battery_id))},
            "name": "Beem Battery",
            "manufacturer": "Beem",
            "model": "Beem Battery",
            "configuration_url": "https://beem.energy/",
        }

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self.async_write_ha_state))
