<!--
---
name: ArduPilot
class: interface
type: pinout
description: T3 Gemstone O1 header functions used by ArduPilot
url: https://docs.t3gemstone.org/en/projects/ardupilot
pin:
  '3':
    name: GPS / ADS1115 SDA
  '5':
    name: GPS / ADS1115 SCL
  '7':
    name: GPS RX
  '8':
    name: RCOut 2
  '10':
    name: RCIn SBUS
  '11':
    name: GPS TX
  '12':
    name: RCOut 7
  '18':
    name: Telemetry TX
  '19':
    name: SPI MOSI
  '21':
    name: SPI MISO
  '23':
    name: SPI SCLK
  '24':
    name: SPI CS0
  '26':
    name: Telemetry RX
  '27':
    name: Reserved I2C SDA
  '28':
    name: Reserved I2C SCL
  '29':
    name: RCOut 1
  '31':
    name: RCOut 3
  '32':
    name: RCOut 5
  '33':
    name: RCOut 4
  '36':
    name: RCOut 6
  '37':
    name: Buzzer
-->

# ArduPilot GPIO connections

This section shows the functions assigned to the 40-pin header by the official T3 Gemstone ArduPilot configuration once the required device tree overlays are enabled.

## Navigation and control

* **GPS and external compass:** pins 7 (UART-MAIN6 RX), 11 (UART-MAIN6 TX), 3 (I2C-MCU0 SDA) and 5 (I2C-MCU0 SCL) are used.
* **RC input:** pin 10 (UART-MAIN1 RX) supports the SBUS signal.
* **RC outputs:** pins 29, 8, 31, 33, 32, 36 and 12 provide RCOut 1-7 respectively.
* **Telemetry:** pins 18 (UART-WKUP0 TX) and 26 (UART-WKUP0 RX) are used.

## Other assigned pins

Pins 19, 21, 23 and 24 form the SPI-MCU0 interface. Pins 27 and 28 are reserved for I2C-WKUP0, while pin 37 is assigned to an external buzzer connection.

> **SBUS warning:** SBUS uses an inverted serial signal. Connect an external signal inverter between the receiver and pin 10. Do not connect a standard SBUS output directly to pin 10.

> **Power and logic warning:** The RCOut pins provide a PWM signal at 3.3 V logic levels only and do not supply power for servos. Power servos and other external loads from an external supply with a sufficient current rating that shares a common ground with the board. Use a suitable driver circuit or logic level converter where required. Before connecting GPS and telemetry devices, verify that their signal levels match 3.3 V logic levels.

Before wiring peripherals, enable the required device tree overlays listed in the official T3 Gemstone documentation. That guide also describes Linux device paths, service configuration and QGroundControl connectivity.
