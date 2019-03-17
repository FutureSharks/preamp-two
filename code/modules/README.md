# Modules and example code

Example for `mdac_attenuator.py`:

```python
import board
import busio
import digitalio
from mdac_attenuator import MdacAttenuator

cs = digitalio.DigitalInOut(board.A4)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

attenuator = MdacAttenuator(spi, cs)

# Set low volume
attenuator._write_level(1)

# Set high volume
attenuator._write_level(65000)
```

Example for `input_selector.py`:

```python
import board
import busio
import digitalio
from input_selector import InputSelector

cs = digitalio.DigitalInOut(board.A4)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

input_selector = InputSelector(spi, cs)

# Toggle mute
input_selector.toggle_mute()

# Select specific inputs
input_selector.select_input(1)
input_selector.select_input(3)

# Selecto next input
input_selector.next_input()
```

Example for `encoder_panel.py`:

```python
import board
from encoder_panel import EncoderPanel

encoder1 = EncoderPanel(
    pixel_pin=board.D9,
    encoder_pin_a=board.D5,
    encoder_pin_b=board.D7
)

# Read encoder value
encoder1.read_encoder()
```
