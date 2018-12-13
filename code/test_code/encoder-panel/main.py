import board
import encoder_panel


encoder1 = encoder_panel.EncoderPanel(
    pixel_pin=board.D10,
    encoder_pin_a=board.D11,
    encoder_pin_b=board.D12
)

encoder1.read_encoder()
