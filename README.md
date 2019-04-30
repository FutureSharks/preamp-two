# Preamp Two

<a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/page_break_input_selector.png" width="900"></a>

![complete](images/complete_1.jpg)

Here is my project to build a Hi-Fi preamplifier. This repository includes schematics, PCB layouts, CircuitPython code, BoMs, measurements and photos.

Features:

* High performance design with measurements
* Quality components
* Completely digitally Controlled
* Modular design
* All open source

![prototype](images/prototypes/prototype-16.gif)

![complete](images/complete_2.jpg)

![complete](images/complete_3.jpg)

![complete](images/complete_4.jpg)

![prototype](images/diagram.png)

### Components

<a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/page_break_input_selector.png" width="900"></a>

The preamplifier is made up of a number of connected components:

* MDAC attenuator ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/mdac-attenuator), [code](https://github.com/FutureSharks/preamp-two/tree/master/code/modules/mdac_attenuator.py)): Controls the volume
* Input selector ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/input-selector), [code](https://github.com/FutureSharks/preamp-two/tree/master/code/modules/input_selector.py)): Selects the input
* Encoder panel ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/encoder-panel), [code](https://github.com/FutureSharks/preamp-two/tree/master/code/modules/encoder_panel.py)): Holds rotary encoder and LED indicator
* Power Supply 5V ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/psu-digital)): Power supply for digital components.
* Power Supply +/- 15V ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/psu-analog)): Power supply for MDAC attenuator op-amp
* Micro controller board ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/mcu-board)): Holds the micro controller and other connectors
* RCA panel ([PCB](https://github.com/FutureSharks/preamp-two/tree/master/PCBs/rca-panel)): For the RCA sockets and connectors

The PCBs and schematics were created in [KiCad](http://kicad-pcb.org/) and the code that runs on the micro controller is [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython).

<a href="https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-adafruit_blinka_angles-left.svg?sanitize=true" width="60"></a>      <a href="https://www.oshwa.org/"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-oshw-outline.svg?sanitize=true" width="60"></a>      <a href="http://kicad-pcb.org/"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-kicad.png" width="60"></a>

### Prototypes and testing

<a href="#"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/page_break_input_selector.png" width="900"></a>

See here: [images/prototypes](images/prototypes)

PCBs made by [OSH Park](https://oshpark.com/).
