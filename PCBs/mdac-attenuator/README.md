# MDAC attenuator

![page break](../../../master/images/page_break_mdac_attenuator.png?raw=true)

Based on designs from these sources:

- [Precision, AC Reference Signal Attenuator Using the AD5546/AD5556 Multiplying DAC](https://www.analog.com/media/en/technical-documentation/application-notes/AN-1488.pdf)
- [New High-Resolution Multiplying DACs Excel at Handling AC Signals](https://www.analog.com/en/analog-dialogue/articles/high-resolution-multiplying-dacs.html)

This design is also used by a number manufacturers:

- Mark Levinson preamps
- Luxman LECUA (Luxman Electronically Controlled Ultimate Attenuator)
- Accuphase [AAVA](http://www.accuphase.com/aava.html)

Features:

* 65536 linear steps
* Gain possible, set by op-amp and resistors
* Excellent performance
* Can drive headphones
* Compact
* SPI controlled

Here is the DIYAudio forum thread with my prototypes and questions: [Solid state R2R attenuator using analog switches or multiplying DAC](https://www.diyaudio.com/forums/analog-line-level/235853-solid-r2r-attenuator-using-analog-switches-multiplying-dac.html)

### Photos

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/mdac_attenuator_3d.png" width="600">

### Code

CircuitPython module is here: [code/modules/input_selector.py](https://github.com/FutureSharks/preamp-two/blob/master/code/modules/mdac_attenuator.py)

### Schematic

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/mdac_attenuator_schematic.png" width="900">

### Layout

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/mdac_attenuator_pcb_front.png" width="900">

<img src="https://raw.githubusercontent.com/FutureSharks/preamp-two/master/images/mdac_attenuator_pcb_back.png" width="900">

### BoM

| Reference                |  Quantity |  Value  |  Footprint / Notes  |
|--------------------------|-----------|---------|------------------|
| C1A1, C1B1               | 2         | 2pF           | 0805       |
| C4, C6, C7               | 3         | 100nF         | 1206       |
| C2, C3, C5               | 3         | 100uF         | Radial 10/5mm or SMD |
| IN1, OUT1, PWR1          | 3         | 1x3           | Molex KK 254, Multicomp MC34 or any 0.1" socket header |
| J1                       | 1         | 1x6           | Molex KK 254, Multicomp MC34 or any 0.1" socket header |
| J2                       | 1         | 1x6           | 0.1" socket header, for passthrough to input-selector |
| LED1                     | 1         | LED           | 1206 |
| R1                       | 1         | RLED          | 1206 |
| R1A1, R1B1               | 2         | 91R           | 1206 |
| R2A1, R2B1, R4A1, R4B1   | 4         | 120R          | 1206 |
| R3A1, R3B1               | 2         | 360R          | 1206 |
| U1                       | 1         | AD8599ARZ     | SOIC-8 |
| U2                       | 1         | DAC8812ICPWG4 | TSSOP-16 | Can also use AD5545

Values for R1, R2 and R3 above give a gain of 4.

To calculate gain use this formula:

```
gain = (R2+R3)/R2
R1 = (R2*R3)/(R2+R3)
```

Refer to the [AD5429/AD5439/AD5449 datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD5429_5439_5449.pdf)
