# MDAC attenuator

![page break](../../../master/images/page-break-mdac-attenuator.png?raw=true)

### BoM

| Reference                |  Quantity |  Value  |  Footprint       |
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
| U2                       | 1         | DAC8812ICPWG4 | TSSOP-16 |

Values for R1, R2 and R3 above give a gain of 4.

To calculate gain use this formula:

```
gain = (R2+R3)/R2
R1 = (R2*R3)/(R2+R3)
```

This was copied from the [AD5429/AD5439/AD5449 datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD5429_5439_5449.pdf)

### Images

![pcb front](../../../master/images/mdac-attenuator-pcb-front.png?raw=true)
