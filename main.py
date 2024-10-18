import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT
status.value = 0

orangeLED = DigitalInOut(board.IO18)
orangeLED.direction = Direction.OUTPUT
orangeLED.value = 0

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36, 
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]


for led in leds:
    led.direction = Direction.OUTPUT

sleep_inc = 1/120 #120 fps-ish
min_vol = 22000
max_vol = 55000
inc_offset = 2000
vol_inc = max_vol/(len(leds) + 1) - inc_offset
print(vol_inc)
print("initializing loop!")
# main loop
while True:
    volume = microphone.value  # max value 60748

    print(volume)
    for n in range(len(leds)):
        current_inc = min_vol + vol_inc * n
        if current_inc < volume:
            leds[n].value = True

        else:
            leds[n].value = False

    #        led.value = not led.value
    #        sleep(0.5)
    #        led.value = not led.value

    #        (led+1).value = not (led+1).value
    #    leds[0].value = not leds[0].value
    #    leds[1].value = not leds[0].value

    sleep(sleep_inc)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?