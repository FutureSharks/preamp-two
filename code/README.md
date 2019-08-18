# Code

[![](../images/page-break-4.png)](#)

Here is the code to run on a [CircuitPython](https://circuitpython.org/) micro-controller. Written and tested with Version 4.1.

To copy the code to the micro-controller:

```
cp -a code/modules code/main.py /Volumes/CIRCUITPY/
```

## Modules

- `modules/encoder_panel.py`: Controls the NeoPixel ring and reads the rotary encoder
- `modules/input_selector.py`: Controls the input selector hardware
- `modules/mdac_attenuator.py`: Controls the input attenuator hardware
- `modules/volume_control.py`: Manages the volume control interface
-	`modules/input_control.py`: Manages the input selector interface

---

<a href="https://circuitpython.org/"><img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/logo-adafruit_blinka_angles-left.svg?sanitize=true" width="60"></a>
