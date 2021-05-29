#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace victron {

class VictronComponent : public uart::UARTDevice, public Component {
 public:
  void set_max_power_yesterday_sensor(sensor::Sensor *max_power_yesterday_sensor) { max_power_yesterday_sensor_ = max_power_yesterday_sensor; }
  void set_max_power_today_sensor(sensor::Sensor *max_power_today_sensor) { max_power_today_sensor_ = max_power_today_sensor; }
  void set_yield_total_sensor(sensor::Sensor *yield_total_sensor) { yield_total_sensor_ = yield_total_sensor; }
  void set_yield_yesterday_sensor(sensor::Sensor *yield_yesterday_sensor) { yield_yesterday_sensor_ = yield_yesterday_sensor; }
  void set_yield_today_sensor(sensor::Sensor *yield_today_sensor) { yield_today_sensor_ = yield_today_sensor; }
  void set_panel_voltage_sensor(sensor::Sensor *panel_voltage_sensor) { panel_voltage_sensor_ = panel_voltage_sensor; }
  void set_panel_power_sensor(sensor::Sensor *panel_power_sensor) { panel_power_sensor_ = panel_power_sensor; }
  void set_battery_voltage_sensor(sensor::Sensor *battery_voltage_sensor) { battery_voltage_sensor_ = battery_voltage_sensor; }
  void set_battery_current_sensor(sensor::Sensor *battery_current_sensor) { battery_current_sensor_ = battery_current_sensor; }
  void set_day_number_sensor(sensor::Sensor *day_number_sensor) { day_number_sensor_ = day_number_sensor; }

  void dump_config() override;
  void loop() override;

  float get_setup_priority() const { return setup_priority::DATA; }

 protected:
  void handle_value_();

  sensor::Sensor *max_power_yesterday_sensor_{nullptr};
  sensor::Sensor *max_power_today_sensor_{nullptr};
  sensor::Sensor *yield_total_sensor_{nullptr};
  sensor::Sensor *yield_yesterday_sensor_{nullptr};
  sensor::Sensor *yield_today_sensor_{nullptr};
  sensor::Sensor *panel_voltage_sensor_{nullptr};
  sensor::Sensor *panel_power_sensor_{nullptr};
  sensor::Sensor *battery_voltage_sensor_{nullptr};
  sensor::Sensor *battery_current_sensor_{nullptr};
  sensor::Sensor *day_number_sensor_{nullptr};

  int state_{0};
  std::string label_;
  std::string value_;
  uint32_t last_transmission_{0};
};

}  // namespace victron
}  // namespace esphome
