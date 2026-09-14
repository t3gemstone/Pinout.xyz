<!--
---
name: PCM
class: interface
type: pinout
description: T3 Gemstone O1 PCM/I2S-compatible header signals
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pin:
  '12':
    name: CLK
  '35':
    name: FS
  '38':
    name: DATA0
  '40':
    name: DATA1
-->

# PCM - Pulse-code Modulation

Four pins are used for the digital audio interface, in the same physical pin positions that the Raspberry Pi uses for its I2S interface. For that reason a Raspberry Pi compatible audio HAT can be plugged into the header physically.

| Pin | Function |
| --: | :-- |
| 12 | Bit clock (CLK) |
| 35 | Frame sync (FS) |
| 38 | Audio data |
| 40 | Audio data |

On the T3 Gemstone O1 both audio data pins can be configured as an input or an output in software. The direction of the data pins is determined by the audio configuration in use rather than by the physical wiring.
