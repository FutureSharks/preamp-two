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

## Bill of materials

### Input selector

| Part name                         | Farnell Part | Detail                                                                                                        | Description        | Notes | Quantity |
|-----------------------------------|--------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------|----------|
| K1-6                              | 1867255      | AGQ2104H                                                                                                      | 1 coil latching    |       | 6        |
| KMUTE                             | 3104813      | AGQ2004H                                                                                                      | Single side stable |       | 1        |
| IC1                               | -            | MCP23S17SO                                                                                                    |                    |       | 1        |
| IC2, IC3                          | -            | ULN2803                                                                                                       |                    |       | 2        |
| R1-12                             | -            |                                                                                                               | 47R, 1206          |       | 12       |
| EXTRA_IO                          | 1675765      | MULTICOMP MC34631 Wire-To-Board Connector, Vertical, MC34 Series, Through Hole, Header, 3, 2.54 mm            |                    |       | 1        |
| X1                                | 1675768      | MULTICOMP MC34635 Wire-To-Board Connector, MC34 Series, Through Hole, Header, 6, 2.54 mm, Tin Plated Contacts |                    |       | 1        |
| POWER                             | 1675764      | MULTICOMP MC34629 Wire-To-Board Connector, Vertical, MC34 Series, Through Hole, Header, 2, 2.54 mm            |                    |       | 1        |
| IN1-6, SEL_OUT, MUTE_IN, MUTE_OUT | 1675765      | MULTICOMP MC34631 Wire-To-Board Connector, Vertical, MC34 Series, Through Hole, Header, 3, 2.54 mm            |                    |       | 9        |
| C2                                | -            | Panasonic E/D SMD (8/6.3mm) or 3.5/8mm leaded                                                                 |                    |       | 1        |
| C1                                | 1414725      | KEMET - C1206C224K5RACTU                                                                                      |                    |       | 1        |
| LED                               | 2217976      | 1206 LED                                                                                                      |                    |       | 1        |
| RLED                              | -            | 1206 Resistor, 1.2K                                                                                           |                    |       | 1        |

### MDAC attenuator

To calculate gain use this formula:

      gain = (R2+R3)/R2
      R1 = (R2*R3)/(R2+R3)

This was copied from the [AD5429/AD5439/AD5449 datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD5429_5439_5449.pdf)

| Part name    | Farnell Part | Detail                     | Description                                      | Notes            | Quantity |
|--------------|--------------|----------------------------|--------------------------------------------------|------------------|----------|
| U2           | 1390687      | TI DAC8812ICPWG4           |                                                  |                  | 1        |
| IC2          | 1438872      | ANALOG DEVICES - AD8599ARZ | Description: IC, OP AMP, DUAL, SMD, SOIC8, 8599  |                  | 1        |
| C1A, C1B     | 1759181      | MULTICOMP - MCCA000310     | Description: CAP, MLCC, C0G/NP0, 2PF, 50V, 0805  |                  | 2        |
| R1A/B        | 1841733      | PANASONIC - ERA8AEB910V    | Description: RESISTOR, 1206, 0.1%, 0.25W, 91R    | 91R (gain of 4)  | 2        |
| R2A/B, R4A/B | 1841735      | PANASONIC - ERA8AEB121V    | Description: RESISTOR, 1206, 0.1%, 0.25W, 120R   | 120R (gain of 4) | 4        |
| R3A/B        | 1841744      | PANASONIC - ERA8AEB361V    | Description: RESISTOR, 1206, 0.1%, 0.25W, 360R   | 360R (gain of 4) | 2        |
| C7           | -            | -                          | Panasonic D/C SMD (6.3/5mm) or 3.5/8mm leaded    |                  | 1        |
| C6, C6       | -            | -                          | Panasonic E/D SMD (8/6.3mm) or 3.5/8mm leaded    |                  | 2        |
| X1           | 1675777      | MULTICOMP MC34649          | Description: HEADER, THT, VERTICAL, 2.54MM, 6WAY |                  | 1        |
| IN, OUT, PWR | 1675765      | MULTICOMP - MC34631        | Description: HEADER, THT, VERTICAL, 2.54MM, 3WAY |                  | 3        |
| C2, C3, C4   | 1414725      | KEMET - C1206C224K5RACTU   | Description: CAP, MLCC, X7R, 220NF, 50V, 1206    |                  | 3        |
| LED          | 2217976      | 1206 LED                   | Description: LED, SMD, 1206 BLUE                 |                  | 1        |
| RLED         | -            | 1206 Resistor, 1.2K        |                                                  |                  | 1        |
