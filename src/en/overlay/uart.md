<!--
---
name: UART
class: interface
type: pinout
description: T3 Gemstone O1 UART-MAIN1 header pins and optional UART routes
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/serial
pin:
  '8':
    name: UART-MAIN1 TX
    direction: output
    active: high
  '10':
    name: UART-MAIN1 RX
    direction: input
    active: high
  '11':
    name: UART-MAIN1 RTS
    direction: output
    active: low
  '36':
    name: UART-MAIN1 CTS
    direction: input
    active: low
-->

# UART

Physical Pin 8 is used to send data (TX) and Physical Pin 10 to receive it (RX). In Linux this serial port appears as the /dev/ttyS3 device. When wiring, connect the RX line of the external device to Physical Pin 8 and its TX line to Physical Pin 10, and connect the grounds of the device and the board together.

Physical Pin 11 and Physical Pin 36 can be used as the RTS and CTS lines respectively, for devices that need flow control. Simple serial communication applications generally do not need these lines and they can be left unconnected.

> **Use 3.3 V logic levels only:** Do not connect this serial port directly to an RS-232 interface or to a serial converter with 5 V logic levels. Such connections can damage the board. For a USB serial connection, use a USB-to-serial converter that supports 3.3 V logic levels, or a suitable RS-232 level converter.

The three-pin connector on the board is a separate serial port reserved for the boot console. This connector is not the same interface as the serial port on Physical Pin 8, Physical Pin 10, Physical Pin 11 and Physical Pin 36.
