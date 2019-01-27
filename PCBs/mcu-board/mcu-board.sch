EESchema Schematic File Version 4
LIBS:mcu-board-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_01x05 ENCODER-PANEL-2
U 1 1 5C266616
P 6000 1600
F 0 "ENCODER-PANEL-2" V 5966 1312 50  0000 R CNN
F 1 "ENCODER-PANEL-2" V 5875 1312 50  0000 R CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 6000 1600 50  0001 C CNN
F 3 "~" H 6000 1600 50  0001 C CNN
	1    6000 1600
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x05 ENCODER-PANEL-1
U 1 1 5C26667B
P 4650 1600
F 0 "ENCODER-PANEL-1" V 4616 1312 50  0000 R CNN
F 1 "ENCODER-PANEL-1" V 4525 1312 50  0000 R CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 4650 1600 50  0001 C CNN
F 3 "~" H 4650 1600 50  0001 C CNN
	1    4650 1600
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x06 J5
U 1 1 5C266772
P 9100 1600
F 0 "J5" V 8973 1880 50  0000 L CNN
F 1 "MDAC-INPUT-SELECTOR" V 9064 1880 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-06A_1x06_P2.54mm_Vertical" H 9100 1600 50  0001 C CNN
F 3 "~" H 9100 1600 50  0001 C CNN
	1    9100 1600
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 5V1
U 1 1 5C26682E
P 7150 1600
F 0 "5V1" H 7229 1592 50  0000 L CNN
F 1 "5V" H 7229 1501 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 7150 1600 50  0001 C CNN
F 3 "~" H 7150 1600 50  0001 C CNN
	1    7150 1600
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 3.3V1
U 1 1 5C2668A5
P 7700 1600
F 0 "3.3V1" H 7779 1592 50  0000 L CNN
F 1 "3.3V" H 7779 1501 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 7700 1600 50  0001 C CNN
F 3 "~" H 7700 1600 50  0001 C CNN
	1    7700 1600
	0    -1   -1   0   
$EndComp
$Comp
L adafruit-itsybitsy:m0-express U1
U 1 1 5C26DA4B
P 5900 4400
F 0 "U1" H 5900 5225 50  0000 C CNN
F 1 "m0-express" H 5900 5134 50  0000 C CNN
F 2 "m0-express:m0-express" H 5950 4400 50  0001 C CNN
F 3 "" H 5950 4400 50  0001 C CNN
	1    5900 4400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5C26DC76
P 7150 2200
F 0 "#PWR0101" H 7150 1950 50  0001 C CNN
F 1 "GND" H 7155 2027 50  0000 C CNN
F 2 "" H 7150 2200 50  0001 C CNN
F 3 "" H 7150 2200 50  0001 C CNN
	1    7150 2200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5C26DC94
P 7700 2200
F 0 "#PWR0102" H 7700 1950 50  0001 C CNN
F 1 "GND" H 7705 2027 50  0000 C CNN
F 2 "" H 7700 2200 50  0001 C CNN
F 3 "" H 7700 2200 50  0001 C CNN
	1    7700 2200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 5C26DCAB
P 5800 2100
F 0 "#PWR0103" H 5800 1850 50  0001 C CNN
F 1 "GND" H 5805 1927 50  0000 C CNN
F 2 "" H 5800 2100 50  0001 C CNN
F 3 "" H 5800 2100 50  0001 C CNN
	1    5800 2100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 5C26DCC2
P 4450 2150
F 0 "#PWR0104" H 4450 1900 50  0001 C CNN
F 1 "GND" H 4455 1977 50  0000 C CNN
F 2 "" H 4450 2150 50  0001 C CNN
F 3 "" H 4450 2150 50  0001 C CNN
	1    4450 2150
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0105
U 1 1 5C26E159
P 7800 1900
F 0 "#PWR0105" H 7800 1750 50  0001 C CNN
F 1 "+3V3" H 7815 2073 50  0000 C CNN
F 2 "" H 7800 1900 50  0001 C CNN
F 3 "" H 7800 1900 50  0001 C CNN
	1    7800 1900
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR0106
U 1 1 5C26E219
P 7250 1900
F 0 "#PWR0106" H 7250 1750 50  0001 C CNN
F 1 "+5V" H 7265 2073 50  0000 C CNN
F 2 "" H 7250 1900 50  0001 C CNN
F 3 "" H 7250 1900 50  0001 C CNN
	1    7250 1900
	-1   0    0    1   
$EndComp
Wire Wire Line
	7150 1800 7150 2200
Wire Wire Line
	7700 1800 7700 2200
Wire Wire Line
	7800 1800 7800 1900
Wire Wire Line
	7250 1800 7250 1900
$Comp
L power:GND #PWR0107
U 1 1 5C26E452
P 8900 1850
F 0 "#PWR0107" H 8900 1600 50  0001 C CNN
F 1 "GND" H 8905 1677 50  0000 C CNN
F 2 "" H 8900 1850 50  0001 C CNN
F 3 "" H 8900 1850 50  0001 C CNN
	1    8900 1850
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0108
U 1 1 5C26E500
P 9000 2100
F 0 "#PWR0108" H 9000 1950 50  0001 C CNN
F 1 "+3V3" H 9015 2273 50  0000 C CNN
F 2 "" H 9000 2100 50  0001 C CNN
F 3 "" H 9000 2100 50  0001 C CNN
	1    9000 2100
	-1   0    0    1   
$EndComp
Wire Wire Line
	8900 1800 8900 1850
Wire Wire Line
	9000 2100 9000 1800
$Comp
L power:+5V #PWR0109
U 1 1 5C26E893
P 5900 1850
F 0 "#PWR0109" H 5900 1700 50  0001 C CNN
F 1 "+5V" H 5915 2023 50  0000 C CNN
F 2 "" H 5900 1850 50  0001 C CNN
F 3 "" H 5900 1850 50  0001 C CNN
	1    5900 1850
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR0110
U 1 1 5C26E8AA
P 4550 1850
F 0 "#PWR0110" H 4550 1700 50  0001 C CNN
F 1 "+5V" H 4565 2023 50  0000 C CNN
F 2 "" H 4550 1850 50  0001 C CNN
F 3 "" H 4550 1850 50  0001 C CNN
	1    4550 1850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 1800 4550 1850
Wire Wire Line
	5900 1800 5900 1850
Wire Wire Line
	4450 1800 4450 2150
Wire Wire Line
	5800 1800 5800 2100
$Comp
L Connector_Generic:Conn_01x02 VBAT1
U 1 1 5C26EEAE
P 8250 1600
F 0 "VBAT1" H 8329 1592 50  0000 L CNN
F 1 "V-BAT" H 8329 1501 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 8250 1600 50  0001 C CNN
F 3 "~" H 8250 1600 50  0001 C CNN
	1    8250 1600
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 5C26EEFA
P 8250 2200
F 0 "#PWR0111" H 8250 1950 50  0001 C CNN
F 1 "GND" H 8255 2027 50  0000 C CNN
F 2 "" H 8250 2200 50  0001 C CNN
F 3 "" H 8250 2200 50  0001 C CNN
	1    8250 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	8250 1800 8250 2200
Wire Wire Line
	5450 3900 5200 3900
Wire Wire Line
	5200 3900 5200 3600
$Comp
L power:+3V3 #PWR0112
U 1 1 5C3B40C6
P 5200 3600
F 0 "#PWR0112" H 5200 3450 50  0001 C CNN
F 1 "+3V3" H 5215 3773 50  0000 C CNN
F 2 "" H 5200 3600 50  0001 C CNN
F 3 "" H 5200 3600 50  0001 C CNN
	1    5200 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 4000 6650 4000
Wire Wire Line
	6350 3900 6850 3900
$Comp
L power:GND #PWR0113
U 1 1 5C3B43EE
P 6850 3900
F 0 "#PWR0113" H 6850 3650 50  0001 C CNN
F 1 "GND" H 6855 3727 50  0000 C CNN
F 2 "" H 6850 3900 50  0001 C CNN
F 3 "" H 6850 3900 50  0001 C CNN
	1    6850 3900
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0114
U 1 1 5C3B441C
P 6650 4000
F 0 "#PWR0114" H 6650 3850 50  0001 C CNN
F 1 "+5V" H 6665 4173 50  0000 C CNN
F 2 "" H 6650 4000 50  0001 C CNN
F 3 "" H 6650 4000 50  0001 C CNN
	1    6650 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	5450 4800 5050 4800
Wire Wire Line
	5450 4900 5050 4900
Text GLabel 5050 4800 0    50   Input ~ 0
SCK
Text GLabel 5050 4900 0    50   Input ~ 0
MOSI
Wire Wire Line
	9100 1800 9100 2350
Text GLabel 9100 2350 3    50   Input ~ 0
CS_input_selector
Wire Wire Line
	9200 1800 9200 2350
Text GLabel 9200 2350 3    50   Input ~ 0
SCK
Text GLabel 9300 2350 3    50   Input ~ 0
CS_mdac_attenuator
Wire Wire Line
	9300 1800 9300 2350
Wire Wire Line
	9400 1800 9400 2350
Text GLabel 9400 2350 3    50   Input ~ 0
MOSI
Text GLabel 5050 4600 0    50   Input ~ 0
CS_input_selector
Text GLabel 5050 4700 0    50   Input ~ 0
CS_mdac_attenuator
Wire Wire Line
	5450 4600 5050 4600
Wire Wire Line
	5450 4700 5050 4700
$Comp
L SN74AHCT125:SN74AHCT125 U3
U 1 1 5C48D1E6
P 3250 3500
F 0 "U3" V 3197 3928 60  0000 L CNN
F 1 "SN74AHCT125DR" V 3303 3928 60  0000 L CNN
F 2 "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm" H 3250 3350 60  0001 C CNN
F 3 "" H 3250 3350 60  0000 C CNN
	1    3250 3500
	0    1    1    0   
$EndComp
Wire Wire Line
	3050 2650 3050 2350
Wire Wire Line
	3350 2650 3350 2350
Text GLabel 3450 2350 1    50   Input ~ 0
panel_1_neopixel_3v
Text GLabel 3150 2350 1    50   Input ~ 0
panel_2_neopixel_3v
Text GLabel 6600 4500 2    50   Input ~ 0
panel_1_neopixel_3v
Text GLabel 6600 4200 2    50   Input ~ 0
panel_2_neopixel_3v
Text GLabel 3050 2350 1    50   Input ~ 0
panel_2_neopixel_5v
Text GLabel 3350 2350 1    50   Input ~ 0
panel_1_neopixel_5v
Wire Wire Line
	3550 2650 3550 2600
Wire Wire Line
	3550 2600 3250 2600
Wire Wire Line
	3250 2650 3250 2600
Connection ~ 3250 2600
Wire Wire Line
	3250 2600 2950 2600
Wire Wire Line
	2950 2650 2950 2600
$Comp
L power:GND #PWR0115
U 1 1 5C491D54
P 2800 2700
F 0 "#PWR0115" H 2800 2450 50  0001 C CNN
F 1 "GND" H 2805 2527 50  0000 C CNN
F 2 "" H 2800 2700 50  0001 C CNN
F 3 "" H 2800 2700 50  0001 C CNN
	1    2800 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3150 4350 3150 4450
Wire Wire Line
	3150 4450 3450 4450
Wire Wire Line
	3550 4350 3550 4450
Connection ~ 3550 4450
Wire Wire Line
	3450 4350 3450 4450
Connection ~ 3450 4450
Wire Wire Line
	3450 4450 3550 4450
$Comp
L power:+5V #PWR0116
U 1 1 5C494A64
P 3550 4600
F 0 "#PWR0116" H 3550 4450 50  0001 C CNN
F 1 "+5V" H 3565 4773 50  0000 C CNN
F 2 "" H 3550 4600 50  0001 C CNN
F 3 "" H 3550 4600 50  0001 C CNN
	1    3550 4600
	-1   0    0    1   
$EndComp
$Comp
L SN74AHCT125:SN74AHCT125 U2
U 1 1 5C494C70
P 1600 3500
F 0 "U2" V 1547 3928 60  0000 L CNN
F 1 "SN74AHCT125DR" V 1653 3928 60  0000 L CNN
F 2 "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm" H 1600 3350 60  0001 C CNN
F 3 "" H 1600 3350 60  0000 C CNN
	1    1600 3500
	0    1    1    0   
$EndComp
Wire Wire Line
	1900 2650 1900 2550
Wire Wire Line
	1900 2550 1600 2550
Wire Wire Line
	1300 2550 1300 2650
Wire Wire Line
	1600 2650 1600 2550
Connection ~ 1600 2550
Wire Wire Line
	1600 2550 1300 2550
Wire Wire Line
	1500 4350 1500 4450
Wire Wire Line
	1500 4450 1100 4450
Wire Wire Line
	1800 4350 1800 4450
Wire Wire Line
	1800 4450 1500 4450
Connection ~ 1500 4450
Wire Wire Line
	1100 4450 1100 4550
$Comp
L power:GND #PWR0117
U 1 1 5C49A6A9
P 1100 4550
F 0 "#PWR0117" H 1100 4300 50  0001 C CNN
F 1 "GND" H 1105 4377 50  0000 C CNN
F 2 "" H 1100 4550 50  0001 C CNN
F 3 "" H 1100 4550 50  0001 C CNN
	1    1100 4550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 5C49A6FD
P 1150 2700
F 0 "#PWR0118" H 1150 2450 50  0001 C CNN
F 1 "GND" H 1155 2527 50  0000 C CNN
F 2 "" H 1150 2700 50  0001 C CNN
F 3 "" H 1150 2700 50  0001 C CNN
	1    1150 2700
	1    0    0    -1  
$EndComp
Text GLabel 1500 2350 1    50   Input ~ 0
panel_2_encoder_A_5v
Text GLabel 1800 2350 1    50   Input ~ 0
panel_2_encoder_B_5v
Wire Wire Line
	1500 2650 1500 2350
Wire Wire Line
	1800 2650 1800 2350
Text GLabel 1400 2350 1    50   Input ~ 0
panel_2_encoder_A_3v
Text GLabel 1700 2350 1    50   Input ~ 0
panel_2_encoder_B_3v
Text GLabel 6600 4400 2    50   Input ~ 0
panel_2_encoder_B_3v
Text GLabel 6600 4300 2    50   Input ~ 0
panel_2_encoder_A_3v
Text GLabel 1300 4600 3    50   Input ~ 0
panel_1_encoder_A_3v
Text GLabel 1400 4600 3    50   Input ~ 0
panel_1_encoder_A_5v
Text GLabel 1600 4600 3    50   Input ~ 0
panel_1_encoder_B_3v
Text GLabel 1700 4600 3    50   Input ~ 0
panel_1_encoder_B_5v
Wire Wire Line
	1700 4350 1700 4600
Wire Wire Line
	1400 4600 1400 4350
Text GLabel 6600 4700 2    50   Input ~ 0
panel_1_encoder_B_3v
Text GLabel 6600 4600 2    50   Input ~ 0
panel_1_encoder_A_3v
$Comp
L power:+3V3 #PWR0119
U 1 1 5C4A5722
P 1900 4550
F 0 "#PWR0119" H 1900 4400 50  0001 C CNN
F 1 "+3V3" H 1915 4723 50  0000 C CNN
F 2 "" H 1900 4550 50  0001 C CNN
F 3 "" H 1900 4550 50  0001 C CNN
	1    1900 4550
	-1   0    0    1   
$EndComp
$Comp
L Device:LED LED_3V1
U 1 1 5C4CD178
P 8850 4000
F 0 "LED_3V1" H 8841 4216 50  0000 C CNN
F 1 "LED" H 8841 4125 50  0000 C CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 8850 4000 50  0001 C CNN
F 3 "~" H 8850 4000 50  0001 C CNN
	1    8850 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:LED LED_5V1
U 1 1 5C4CD1DA
P 8850 4450
F 0 "LED_5V1" H 8841 4666 50  0000 C CNN
F 1 "LED" H 8841 4575 50  0000 C CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 8850 4450 50  0001 C CNN
F 3 "~" H 8850 4450 50  0001 C CNN
	1    8850 4450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 5C4CD2B6
P 8500 4750
F 0 "#PWR0120" H 8500 4500 50  0001 C CNN
F 1 "GND" H 8505 4577 50  0000 C CNN
F 2 "" H 8500 4750 50  0001 C CNN
F 3 "" H 8500 4750 50  0001 C CNN
	1    8500 4750
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0121
U 1 1 5C4CD2D7
P 9650 3900
F 0 "#PWR0121" H 9650 3750 50  0001 C CNN
F 1 "+3V3" H 9665 4073 50  0000 C CNN
F 2 "" H 9650 3900 50  0001 C CNN
F 3 "" H 9650 3900 50  0001 C CNN
	1    9650 3900
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0122
U 1 1 5C4CD2F8
P 9650 4350
F 0 "#PWR0122" H 9650 4200 50  0001 C CNN
F 1 "+5V" H 9665 4523 50  0000 C CNN
F 2 "" H 9650 4350 50  0001 C CNN
F 3 "" H 9650 4350 50  0001 C CNN
	1    9650 4350
	1    0    0    -1  
$EndComp
$Comp
L Device:R RLED1
U 1 1 5C4CD386
P 9250 4000
F 0 "RLED1" V 9043 4000 50  0000 C CNN
F 1 "R" V 9134 4000 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9180 4000 50  0001 C CNN
F 3 "~" H 9250 4000 50  0001 C CNN
	1    9250 4000
	0    1    1    0   
$EndComp
$Comp
L Device:R RLED2
U 1 1 5C4CD3E1
P 9250 4450
F 0 "RLED2" V 9043 4450 50  0000 C CNN
F 1 "R" V 9134 4450 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9180 4450 50  0001 C CNN
F 3 "~" H 9250 4450 50  0001 C CNN
	1    9250 4450
	0    1    1    0   
$EndComp
Wire Wire Line
	9400 4450 9650 4450
Wire Wire Line
	9650 4450 9650 4350
Wire Wire Line
	9400 4000 9650 4000
Wire Wire Line
	9650 4000 9650 3900
Wire Wire Line
	9100 4000 9000 4000
Wire Wire Line
	9100 4450 9000 4450
Wire Wire Line
	8700 4450 8500 4450
Wire Wire Line
	8500 4450 8500 4750
Wire Wire Line
	8700 4000 8500 4000
Wire Wire Line
	8500 4000 8500 4450
Connection ~ 8500 4450
Text GLabel 6600 3800 2    50   Input ~ 0
BAT
Wire Wire Line
	6350 3800 6600 3800
Text GLabel 8350 1950 3    50   Input ~ 0
BAT
Wire Wire Line
	8350 1800 8350 1950
Wire Wire Line
	2950 2600 2800 2600
Wire Wire Line
	2800 2600 2800 2700
Connection ~ 2950 2600
Wire Wire Line
	1300 2550 1150 2550
Wire Wire Line
	1150 2550 1150 2700
Connection ~ 1300 2550
Wire Wire Line
	6350 4400 6600 4400
Wire Wire Line
	6350 4500 6600 4500
Wire Wire Line
	6350 4600 6600 4600
Wire Wire Line
	6350 4700 6600 4700
Text GLabel 6000 2050 3    50   Input ~ 0
panel_2_neopixel_5v
Text GLabel 4650 2050 3    50   Input ~ 0
panel_1_neopixel_5v
Text GLabel 6200 2050 3    50   Input ~ 0
panel_2_encoder_B_5v
Text GLabel 6100 2050 3    50   Input ~ 0
panel_2_encoder_A_5v
Text GLabel 4850 2050 3    50   Input ~ 0
panel_1_encoder_B_5v
Text GLabel 4750 2050 3    50   Input ~ 0
panel_1_encoder_A_5v
Wire Wire Line
	6000 1800 6000 2050
Wire Wire Line
	6100 1800 6100 2050
Wire Wire Line
	6200 1800 6200 2050
Wire Wire Line
	4850 1800 4850 2050
Wire Wire Line
	4750 1800 4750 2050
Wire Wire Line
	4650 1800 4650 2050
$Comp
L Mechanical:MountingHole_Pad H1
U 1 1 5C534EFB
P 3600 6000
F 0 "H1" H 3700 6051 50  0000 L CNN
F 1 "MountingHole_Pad" H 3700 5960 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 3600 6000 50  0001 C CNN
F 3 "~" H 3600 6000 50  0001 C CNN
	1    3600 6000
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole_Pad H2
U 1 1 5C534F7C
P 3800 6000
F 0 "H2" H 3900 6051 50  0000 L CNN
F 1 "MountingHole_Pad" H 3900 5960 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 3800 6000 50  0001 C CNN
F 3 "~" H 3800 6000 50  0001 C CNN
	1    3800 6000
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole_Pad H3
U 1 1 5C534FAA
P 3600 6300
F 0 "H3" H 3700 6351 50  0000 L CNN
F 1 "MountingHole_Pad" H 3700 6260 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 3600 6300 50  0001 C CNN
F 3 "~" H 3600 6300 50  0001 C CNN
	1    3600 6300
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole_Pad H4
U 1 1 5C534FDF
P 3800 6300
F 0 "H4" H 3900 6351 50  0000 L CNN
F 1 "MountingHole_Pad" H 3900 6260 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 3800 6300 50  0001 C CNN
F 3 "~" H 3800 6300 50  0001 C CNN
	1    3800 6300
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 IR1
U 1 1 5C535923
P 9800 1600
F 0 "IR1" V 9766 1412 50  0000 R CNN
F 1 "Conn_01x03" V 9675 1412 50  0000 R CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 9800 1600 50  0001 C CNN
F 3 "~" H 9800 1600 50  0001 C CNN
	1    9800 1600
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0123
U 1 1 5C535B57
P 9700 2200
F 0 "#PWR0123" H 9700 1950 50  0001 C CNN
F 1 "GND" H 9705 2027 50  0000 C CNN
F 2 "" H 9700 2200 50  0001 C CNN
F 3 "" H 9700 2200 50  0001 C CNN
	1    9700 2200
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0124
U 1 1 5C535B86
P 9800 1900
F 0 "#PWR0124" H 9800 1750 50  0001 C CNN
F 1 "+3V3" H 9815 2073 50  0000 C CNN
F 2 "" H 9800 1900 50  0001 C CNN
F 3 "" H 9800 1900 50  0001 C CNN
	1    9800 1900
	-1   0    0    1   
$EndComp
Wire Wire Line
	9700 1800 9700 2200
Wire Wire Line
	9800 1800 9800 1900
Wire Wire Line
	9900 1800 9900 2450
Text GLabel 9900 2450 3    50   Input ~ 0
IR_SENSOR
Text GLabel 6600 4100 2    50   Input ~ 0
IR_SENSOR
Wire Wire Line
	6350 4100 6600 4100
$Comp
L Device:C C1
U 1 1 5C55AC33
P 2200 4200
F 0 "C1" H 2315 4246 50  0000 L CNN
F 1 "C" H 2315 4155 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 2238 4050 50  0001 C CNN
F 3 "~" H 2200 4200 50  0001 C CNN
	1    2200 4200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5C55ACED
P 3850 4200
F 0 "C2" H 3965 4246 50  0000 L CNN
F 1 "C" H 3965 4155 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3888 4050 50  0001 C CNN
F 3 "~" H 3850 4200 50  0001 C CNN
	1    3850 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 4450 3850 4450
Wire Wire Line
	3850 4450 3850 4350
Wire Wire Line
	1900 4450 2200 4450
Wire Wire Line
	2200 4450 2200 4350
Wire Wire Line
	1900 4450 1900 4350
Wire Wire Line
	2200 4050 2200 3950
Wire Wire Line
	3850 4050 3850 3950
$Comp
L power:GND #PWR0125
U 1 1 5C565708
P 2200 3950
F 0 "#PWR0125" H 2200 3700 50  0001 C CNN
F 1 "GND" H 2205 3777 50  0000 C CNN
F 2 "" H 2200 3950 50  0001 C CNN
F 3 "" H 2200 3950 50  0001 C CNN
	1    2200 3950
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0126
U 1 1 5C565763
P 3850 3950
F 0 "#PWR0126" H 3850 3700 50  0001 C CNN
F 1 "GND" H 3855 3777 50  0000 C CNN
F 2 "" H 3850 3950 50  0001 C CNN
F 3 "" H 3850 3950 50  0001 C CNN
	1    3850 3950
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 2650 1400 2350
Wire Wire Line
	3150 2650 3150 2350
Wire Wire Line
	1700 2650 1700 2350
Wire Wire Line
	3450 2650 3450 2350
Wire Wire Line
	1300 4600 1300 4350
Wire Wire Line
	1600 4600 1600 4350
Wire Wire Line
	1900 4450 1900 4550
Connection ~ 1900 4450
Wire Wire Line
	3550 4450 3550 4600
Wire Wire Line
	6600 4200 6350 4200
Wire Wire Line
	6350 4300 6600 4300
$Comp
L Graphic:Logo_Open_Hardware_Large #LOGO1
U 1 1 5C596626
P 1200 7150
F 0 "#LOGO1" H 1200 7650 50  0001 C CNN
F 1 "Logo_Open_Hardware_Large" H 1200 6750 50  0001 C CNN
F 2 "" H 1200 7150 50  0001 C CNN
F 3 "~" H 1200 7150 50  0001 C CNN
	1    1200 7150
	1    0    0    -1  
$EndComp
$EndSCHEMATC
