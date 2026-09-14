<!--
---
name: GPIO
class: interface
type: pinout
description: T3 Gemstone O1 general-purpose 3.3 V GPIO pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/gpio
pin:
  '3':
  '5':
  '7':
  '8':
  '10':
  '11':
  '12':
  '13':
  '15':
  '16':
  '18':
  '19':
  '21':
  '22':
  '23':
  '24':
  '26':
  '27':
  '28':
  '29':
  '31':
  '32':
  '33':
  '35':
  '36':
  '37':
  '38':
  '40':
-->

# GPIO - General Purpose Input/Output

The 40-pin header on the T3 Gemstone O1 provides digital GPIO pins operating at 3.3 V logic levels. Each pin can be read as a digital input, driven as a digital output, or configured for an alternate function such as UART, SPI, I2C, PCM and PWM.

Use the `libgpiod` tools to control the GPIO pins from Linux. Use `gpioinfo` to list the GPIO pins, `gpioget` to read a pin state and `gpioset` to set a pin state. Refer to GPIO pins by the GPIO name assigned by the system rather than by the physical pin number.

> **Use 3.3 V logic levels:** The GPIO pins are connected directly to the processor with no protection circuitry in between. Applying 5 V to a GPIO pin can damage the processor and the board. The GPIO pins must be used for signals only. Do not connect loads such as LEDs, buzzers, relays or motors directly to a GPIO pin; use a suitable driver circuit, transistor or relay module for such loads.

Some alternate functions become available once the matching device tree overlay is enabled in `/boot/uEnv.txt`. Until the overlay is enabled, the pin operates as a GPIO.
