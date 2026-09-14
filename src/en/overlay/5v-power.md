<!--
---
name: 5v Power
class: interface
type: pinout
description: T3 Gemstone O1 5 V header supply pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 2
pin:
  '2':
  '4':
-->

# 5 V Power

Physical Pin 2 and Physical Pin 4 supply 5 V for peripherals that need a supply voltage higher than 3.3 V. The signal pins, however, support 3.3 V logic levels only. The fact that a peripheral can be powered from 5 V does not mean that it may apply 5 V logic signals to the GPIO pins.

The 5 V on these pins is not supplied directly from the external power source; it is produced by the power regulator on the board. Depending on the power management configuration, this supply rail can be disabled.

> **Do not feed power in:** Physical Pin 2 and Physical Pin 4 are 5 V outputs. Applying an external 5 V to these pins can cause a conflict with the power regulator on the board and disable the protection circuitry on the power input. For that reason, do not power the board through these pins.
