# Preamp Two

Here is the Arduino code and PCB layout files to build a high fidelity preamplifier. It has the following features:

  * A precision volume control using a R2R multiplying DAC
  * 6 input selector with mute
  * Volume and input control via rotary encoders and infrared remote.
  * Start-up mute.

![All together 1](../master/images/all-together-1.jpg?raw=true)

![All together 2](../master/images/all-together-2.jpg?raw=true)

## Hardware

### MDAC attenuator

Based on a design from a Analog Devices circuit note: http://www.analog.com/en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/CN0025.html

This design is also used by a number manufacturers.

  * 65536 linear steps (16bit)
  * Any gain possible, set by OPAMP and resistors
  * Excellent performance
  * Can drive headphones
  * Compact
  * SPI controlled

![MDAC attenuator 1](../master/images/mdac-attenuator-1.jpg?raw=true)

![MDAC attenuator 2](../master/images/mdac-attenuator-2.jpg?raw=true)

### Input selector

  * 6x inputs
  * Mute for the output
  * SPI controlled using a MCP23S17
  * Latching relays so no constant current draw (mute is not latching, obviously)
  * Uses high quality Panasonic GQ relays (AGQ)

![Input selector 1](../master/images/input-selector-1.jpg?raw=true)

![Input selector 2](../master/images/input-selector-2.jpg?raw=true)

### RCA board

Designed for [CMC 816 RCA](http://www.audio-cmc.com/rca-jacks/rca-jacks-p_29.html) sockets, they can be soldered directly on to the PCB and are easy to find on eBay or Aliexpress etc.

![RCA board 1](../master/images/rca-board-1.jpg?raw=true)

![RCA board 2](../master/images/rca-board-2.jpg?raw=true)

### Infrared remote control

The IRremote library is from here:
https://github.com/z3t0/Arduino-IRremote
