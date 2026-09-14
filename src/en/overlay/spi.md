<!--
---
name: SPI
class: interface
type: pinout
description: T3 Gemstone O1 SPI-MCU0 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 5
pin:
  '19':
    name: SPI-MCU0 MOSI
    direction: output
    active: high
  '21':
    name: SPI-MCU0 MISO
    direction: input
    active: high
  '23':
    name: SPI-MCU0 SCLK
    direction: output
    active: high
  '24':
    name: SPI-MCU0 CS0
    direction: output
    active: low
  '26':
    name: SPI-MCU0 CS2
    direction: output
    active: low
-->

# SPI

The SPI interface uses five pins. Physical Pin 19 sends data (MOSI), Physical Pin 21 receives data (MISO) and Physical Pin 23 carries the clock (SCLK). Physical Pin 24 and Physical Pin 26 are the chip select (CS) lines that determine which connected device is active. Once the matching device tree overlay is enabled, these interfaces appear in Linux as the `/dev/spidev0.0` and `/dev/spidev0.2` device files.

Several devices can share the same MOSI, MISO and SCLK lines, provided that each device is assigned its own chip select line and that devices whose chip select is inactive do not drive the SPI data lines.

## The board's own sensors also use this bus

The barometer and IMU sensors on the board share the SPI data and clock lines with external devices. The sensors have their own chip select (CS) lines, and these lines are not brought out to the 40-pin header. For that reason, SPI communication with a correctly configured external device does not clash with the chip select lines of the sensors.

> **Caution** Use only devices that support 3.3 V logic levels. Make sure the external device does not drive the SPI data lines while its chip select (CS) line is inactive. A device driving the data line while its CS line is inactive can affect the SPI communication of the sensors on the board and cause incorrect sensor readings. In the same way, the sensors on the board driving the data line can affect the communication of the external device.

> **Physical Pin 26 has a second function:** Physical Pin 26 can also be used as the receive (RX) line of an additional serial port. When that function is enabled, only Physical Pin 24 is available as a chip select (CS) line on the SPI interface.
