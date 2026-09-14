# T3 Gemstone O1 Pinout

The T3 Gemstone pinout documents the physical pins, compatibility GPIO numbers and default interfaces of the T3 Gemstone O1 development board. The header uses the widely used Raspberry Pi 40-pin physical layout; the processor, the pin multiplexing options and the software stack, however, are specific to the Texas Instruments AM67A platform.

## Header interfaces

The header provides I2C, SPI, a serial port with flow control, four digital audio signals and 3.3 V GPIO connections. In addition, hardware PWM is available on Physical Pin 29, Physical Pin 31, Physical Pin 32 and Physical Pin 33. Some functions are only available once the matching device tree overlay is enabled in `/boot/uEnv.txt`. Check the boot configuration before connecting any device.

## Compatible HATs and add-ons

The fact that an add-on can be physically connected to the header does not mean that it is electrically or software compatible. The [compatible boards catalogue](/boards) lists only boards reviewed against the T3 Gemstone O1 pin assignment, voltage requirements, pin directions, device tree configuration and Linux driver support.

An add-on must not be treated as compatible with the T3 Gemstone O1 unless its status is shown as **Verified** or **Conditionally compatible** in the catalogue.

Compatibility states:

* **Verified:** Hardware and software compatibility have been tested and verified.
* **Conditionally compatible:** It can work when the stated limitations or the required configurations are met.
* **Incompatible:** It must not be used with the T3 Gemstone O1, or a required feature is not supported.

## Official resources

* [T3 Gemstone O1 documentation](https://docs.t3gemstone.org/en/boards/o1/introduction)
* [GPIO guide](https://docs.t3gemstone.org/en/boards/o1/peripherals/gpio)
* [PWM guide](https://docs.t3gemstone.org/en/boards/o1/peripherals/pwm)
* [Open hardware design files](https://github.com/t3gemstone/hardware)
