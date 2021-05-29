import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_ID, UNIT_VOLT, ICON_FLASH, UNIT_AMPERE, UNIT_WATT, \
    UNIT_WATT_HOURS, ICON_POWER, ICON_CURRENT_AC, ICON_COUNTER, UNIT_EMPTY, ICON_EMPTY, \
    DEVICE_CLASS_POWER, DEVICE_CLASS_CURRENT, DEVICE_CLASS_VOLTAGE, DEVICE_CLASS_EMPTY
from . import victron_ns, VictronComponent, CONF_VICTRON_ID

CONF_MAX_POWER_YESTERDAY = "max_power_yesterday"
CONF_MAX_POWER_TODAY = "max_power_today"
CONF_YIELD_TOTAL = "yield_total"
CONF_YIELD_YESTERDAY = "yield_yesterday"
CONF_YIELD_TODAY = "yield_today"
CONF_PANEL_VOLTAGE = "panel_voltage"
CONF_PANEL_POWER = "panel_power"
CONF_BATTERY_VOLTAGE = "battery_voltage"
CONF_BATTERY_CURRENT = "battery_current"
CONF_DAY_NUMBER = "day_number"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_VICTRON_ID): cv.use_id(VictronComponent),
    cv.Optional(CONF_MAX_POWER_YESTERDAY): sensor.sensor_schema(UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_MAX_POWER_TODAY): sensor.sensor_schema(UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_YIELD_TOTAL): sensor.sensor_schema(UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_YIELD_YESTERDAY): sensor.sensor_schema(UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_YIELD_TODAY): sensor.sensor_schema(UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_PANEL_VOLTAGE): sensor.sensor_schema(UNIT_VOLT, ICON_FLASH, 3, DEVICE_CLASS_VOLTAGE),
    cv.Optional(CONF_PANEL_POWER): sensor.sensor_schema(UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER),
    cv.Optional(CONF_BATTERY_VOLTAGE): sensor.sensor_schema(UNIT_VOLT, ICON_FLASH, 3, DEVICE_CLASS_VOLTAGE),
    cv.Optional(CONF_BATTERY_CURRENT): sensor.sensor_schema(UNIT_AMPERE, ICON_CURRENT_AC, 3, DEVICE_CLASS_CURRENT),
    cv.Optional(CONF_DAY_NUMBER): sensor.sensor_schema(UNIT_EMPTY, ICON_EMPTY, 3, DEVICE_CLASS_EMPTY),
})

def to_code(config):
    victron = yield cg.get_variable(config[CONF_VICTRON_ID])

    if CONF_MAX_POWER_YESTERDAY in config:
        sens = yield sensor.new_sensor(config[CONF_MAX_POWER_YESTERDAY])
        cg.add(victron.set_max_power_yesterday_sensor(sens))

    if CONF_MAX_POWER_TODAY in config:
        sens = yield sensor.new_sensor(config[CONF_MAX_POWER_TODAY])
        cg.add(victron.set_max_power_today_sensor(sens))

    if CONF_YIELD_TOTAL in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_TOTAL])
        cg.add(victron.set_yield_total_sensor(sens))

    if CONF_YIELD_YESTERDAY in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_YESTERDAY])
        cg.add(victron.set_yield_yesterday_sensor(sens))

    if CONF_YIELD_TODAY in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_TODAY])
        cg.add(victron.set_yield_today_sensor(sens))

    if CONF_PANEL_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_PANEL_VOLTAGE])
        cg.add(victron.set_panel_voltage_sensor(sens))

    if CONF_PANEL_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_PANEL_POWER])
        cg.add(victron.set_panel_power_sensor(sens))

    if CONF_BATTERY_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_VOLTAGE])
        cg.add(victron.set_battery_voltage_sensor(sens))

    if CONF_BATTERY_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_CURRENT])
        cg.add(victron.set_battery_current_sensor(sens))

    if CONF_DAY_NUMBER in config:
        sens = yield sensor.new_sensor(config[CONF_DAY_NUMBER])
        cg.add(victron.set_day_number_sensor(sens))
