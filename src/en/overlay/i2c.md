<!--
---
name: I2C
class: interface
type: pinout
description: T3 Gemstone O1 I2C-MCU0 and shared I2C-WKUP0 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/i2c
pin:
  '3':
    name: I2C-MCU0 SDA
    direction: both
    active: high
  '5':
    name: I2C-MCU0 SCL
    direction: both
    active: high
  '27':
    name: I2C-WKUP0 SDA
    direction: both
    active: high
  '28':
    name: I2C-WKUP0 SCL
    direction: both
    active: high
-->

# I2C

Physical Pin 3 (data) and Physical Pin 5 (clock) form the I2C bus reserved for external devices. No device on the board is connected to this bus, so it is dedicated to external devices. The pull-up resistors required for I2C communication are already on the board and no additional resistors are needed.

The I2C bus number can vary depending on the software image in use. The bus can appear as `/dev/i2c-1` or `/dev/i2c-2`. Use the following command to list the available I2C buses:

```bash
ls /dev/i2c-*
```

Use the `i2cdetect` command on a bus to see the connected devices and their I2C addresses.

> **Before connecting:** Use only devices that support 3.3 V logic levels. Every device on the I2C bus must have a unique address; using the same address on more than one device can cause communication conflicts. Before adding external pull-up resistors, take into account that the board already has pull-up resistors fitted.

## Pins 27 and 28 are a shared I2C bus

Physical Pin 27 and Physical Pin 28 belong to the second I2C bus on the board. The pull-up resistors required for this bus are already on the board. The power management IC (PMIC), the real-time clock (RTC) and the EEPROM are connected to this bus internally.

You can connect external I2C devices to these pins. Because the bus is shared with the existing devices, use the `i2cdetect` command to check the I2C addresses already present on the bus before connecting a new device, and use a unique address that does not cause a conflict.

> **Caution:** This I2C bus must be used more carefully than the one on pins 3 and 5. Because the power management IC (PMIC) is connected to this bus, a short circuit, an incorrect voltage or a jammed bus can affect the operation not only of the connected peripheral but of the whole board. Do not change the configuration of the devices already present on the bus. For general-purpose sensor and peripheral connections, the I2C bus on Physical Pin 3 and Physical Pin 5 is recommended. That bus is reserved for external devices.
