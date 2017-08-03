"""
This module shows how to use an 5x7 led matrix.

Pinout of the chip:
  
  ooooo
1 ooooo 12
2 ooooo 11
3 ooooo 10
4 ooooo 9
5 ooooo 8
6 ooooo 7

Connections:

     1
   13078
 C ooooo ^
 B ooooo |
 2 ooooo |
 9 ooooo |
 4 ooooo |
 5 ooooo |
 7 ooooo |
   ---->
"""

import RPi.GPIO as GPIO
import time


def main():
    # mapping pins of the chip to GPIO-pins
    led_gpio = {1: 17, 3: 18, 11: 23, 12: 22}

    # using BCM numbering scheme
    GPIO.setmode(GPIO.BCM)

    # configure all pins as output
    for pin in led_gpio:
        GPIO.setup(led_gpio[pin], GPIO.OUT)

    # turning on each led from top left to bottom right
    while True:
        for x in (0, 1):
            for y in (0, 1):
                led(x, y, True, led_gpio)
                time.sleep(1)
                led(x, y, False, led_gpio)
                time.sleep(1)
        

def led(x, y, on_off, led_gpio):
    """Turn the led at coordinate (x,y) on or off. (0,0) is a top left."""
    xy_pins = {(0, 0): (12, 1),
               (0, 1): (12, 3),
               (1, 0): (11, 1),
               (1, 1): (11, 3)}

    if on_off:
        pin_hi, pin_lo = xy_pins[(x, y)]
    else:
        pin_lo, pin_hi = xy_pins[(x, y)]

    gpio_hi, gpio_lo = led_gpio[pin_hi], led_gpio[pin_lo]

    print("hi", gpio_hi, "lo", gpio_lo)
    GPIO.output(gpio_hi, True)
    GPIO.output(gpio_lo, False)


if __name__ == "__main__":
    main()
