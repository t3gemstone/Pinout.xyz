<!--
---
name: 3v3 Power
class: interface
type: pinout
description: T3 Gemstone O1 3.3 V header supply pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 2
pin:
  '1':
  '17':
-->

# 3.3 V Power

Physical Pin 1 and Physical Pin 17 supply 3.3 V. This is also the voltage all the signal pins work at, so it is the right supply for sensors, small displays and other low-power add-ons.

The board makes this 3.3 V with its own regulator, and shares it with the M.2 slot and the camera, display and USB connectors. So the current you can draw here depends on what else is plugged into the board.

> **Do not feed power in:** These pins are an output, not an input. Putting your own 3.3 V into them pushes against the board's regulator and can damage it.
