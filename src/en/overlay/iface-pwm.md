<!--
---
name: PWM
class: interface
type: pinout
description: T3 Gemstone O1 hardware PWM-capable header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/pwm
pin:
  '29':
    name: PWM-0A
  '31':
    name: PWM-1A
  '32':
    name: PWM-0B
  '33':
    name: PWM-1B
-->

# PWM - Pulse-width Modulation

Four pins can produce a hardware-based PWM signal. This keeps the timing of the PWM signal stable and independent of processor load. These pins are grouped into two pairs:

| Pins | Channels |
| :-- | :-- |
| 29 and 32 | PWM-0A and PWM-0B |
| 31 and 33 | PWM-1A and PWM-1B |

The two pins in a pair use a common PWM frequency, but the duty cycle of each pin can be set independently. This allows a total of four independent duty cycles across two different PWM frequencies.

You can control them through `/sys/class/pwm`.

> **PWM pins do not supply power:** These pins provide a PWM signal at 3.3 V logic levels only. Loads such as servos, motors or LED strips must not be powered directly from the PWM pins. Use a suitable external power supply for such loads, connect the ground of the load to a ground pin on the header, and use a suitable driver circuit or transistor where required.
