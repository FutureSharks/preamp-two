### at42 implementation notes

- All passive components associated with the capacitive sensor (such as the Cs reference capacitors and
associated resistors) should be placed as close to the control chip as is physically possible to assist with EMC compliance

- As a general rule, LEDs that are judged as close must be bypassed with a capacitor that has a typical
value of 1 nF (2)

- Sensor or rear, no ground coverage of sensor or within 5mm of sensor

- Regions of floating metal, or any other conductor, that are in close proximity to sensors of this type (that is, nearer than 10 mm edge to edge) can tend to re-radiate the sensor's electric field and so become
touch-sensitive themselves. Always ground nearby conductive regions. This can be accomplished by a direct wire connection to power supply common, or by means of a 47 nF capacitor back to supply common.

- Always run all three channel connections together as a group and keep them well away from noisy
sources and ground loads.

- Keep the traces as short and thin as possible and space the traces with a gap equal to the track width.

- When routing traces from the electrodes, use a via, if possible, for each electrode to route the traces down to the non-touch side of the board, and then run the traces away on this layer. If this is not possible, and the connecting traces have to be routed on the same layer as the electrodes themselves, always escape the traces as quickly as possible out of the touch area; then regroup the three traces for their path to the sensor chip. It can be useful in some cases to run a thin ground trace alongside these escaping traces to desensitize them to touch. Note that some experimentation is usually necessary.
