# Encoder Panel

<a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/page_break_input_selector.png" width="900"></a>

**work in progress**

The module is the sole human interface to the preamp. It consists of 2 things:

- A high quality optical encoder for changing of the volume and input
- A ring of [NeoPixels](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels) as a visual indicator and to give feedback

### Photos

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/encoder_panel_3d.png" width="600">

### <a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-adafruit_blinka_angles-left.svg?sanitize=true" width="20"></a> Code

CircuitPython module is here: [code/modules/encoder_panel.py](https://github.com/FutureSharks/preamp-two/blob/master/code/modules/encoder_panel.py)

### Schematic

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/encoder_panel_schematic.png" width="900">

### Layout

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/encoder_panel_pcb_front.png" width="600">

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/encoder_panel_pcb_back.png" width="600">

### BoM

| Reference  | Quantity | Value       | Footprint                                                      |
|------------|----------|-------------|----------------------------------------------------------------|
| C1-16      | 16       | 0.1uF       | Capacitor SMD 1206      |
| C17, C18   | 2        | 1000uF      | Capacitor SMD 8x5.4 or Capacitor THT D8.0mm P5.00mm |
| D1-16      | 16       | WS2812B     | LED SMD WS2812B                   |
| J1         | 1        | Conn_01x05  | Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical |
| R1         | 1        | 500R        | Resistor SMD 1206 |
| U1         | 1        | ENA1J-B28   | Bourns ENA1J-B28-L00128L                                       |
