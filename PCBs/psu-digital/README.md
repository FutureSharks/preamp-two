# Digital Power Supply

<a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/page_break_rca_panel.png" width="900"></a>

This the 5V digital power supply. It powers the input selector, digital part of the MDAC attenuator, the NeoPixels in the encoder panels and the encoders.

It uses a LT1763 regulator.

The PCB files are in Eagle format. I will convert them to KiCAD soon.

### Photos

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/psu-digital-1.jpg" width="600">

### <a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-adafruit_blinka_angles-left.svg?sanitize=true" width="20"></a> Code

N/A

### Schematic

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/psu-digital-schematic.jpg" width="900">

### Layout

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/psu-digital-front.jpg" width="900">

### BoM

| Reference   | Footprint / Notes  |
|-------------|--------------------|
| F1 | Fuse holder. Part URL. |
| TR1 | Pads for Block FL2/FL4/FL6/FL8 or EI38 or EI30. Ideally 2x 6VAC. Part URL. |
| B1 | VISHAY DFL1508S bridge rectifier. Part URL. |
| C1 | Panasonic FC 1500UF, 16V. Part URL. |
| L1 | INDUCTOR, 1210 CASE, 10UH. Part URL. |
| L2 | FERRITE BEAD, 0.1OHM, 2A, 1206. Part URL. |
| C2 | 100nF X7R, 1206 package. |
| IC1 | LT1763CS8-5, 5V fixed regulator. Part URL. |
| C3 | C0G/NP0, 10NF, 100V, 1206 package. |
| C4 | Panasonic FK 100UF, 6.3V, SMD. Part URL. |
| C5 | 100nF X7R, 1206 package. |
| R1 | Resistor for LED, 1206 package. |
| LED | 1206 LED |
