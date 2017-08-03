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


class LedMatrix:
    
    def __init__(self, led_gpio, boardmode=GPIO.BCM):
        """Create an led matrix with a configuration that maps led pins to gpio pins."""
        self.led_gpio = led_gpio
        
        self.x_pins = [1, 3, 10, 7, 8]
        self.y_pins = [12, 11, 2, 9, 4, 5, 6]
        
        # using BCM numbering scheme
        GPIO.setmode(boardmode)

        # configure all pins as output
        for pin in led_gpio:
            GPIO.setup(led_gpio[pin], GPIO.OUT)

    def led(self, x, y, on_off):
        """Turn the led at coordinate (x,y) on or off. (0,0) is a top left."""

        pin_hi = self.x_pins[x]
        pin_lo = self.y_pins[y]

        if on_off:
            # swap if necessary
            pin_hi, pin_lo = pin_lo, pin_hi

        gpio_hi, gpio_lo = self.led_gpio[pin_hi], self.led_gpio[pin_lo]

        GPIO.output(gpio_hi, True)
        GPIO.output(gpio_lo, False)


def main():
    # mapping pins of the chip to GPIO-pins
    led_gpio = {1: 17, 3: 18, 11: 23, 12: 22}
    ledm = LedMatrix(led_gpio)

    # turning on each led from top left to bottom right
    start = time.time()
    while time.time() - start < 5:
        for x in (0, 1):
            for y in (0, 1):
                ledm.led(x, y, True)
                time.sleep(0.2)
                ledm.led(x, y, False)
                time.sleep(0.2)

    # turning on some leds using muliplexing
    while True:
        for x in (0, 1):
            for y in (0, 1):
                if (x, y) in [(0, 0), (1, 1)]:
                    ledm.led(x, y, True)
                    time.sleep(0.002)
                    ledm.led(x, y, False)
                    
                else:
                    ledm.led(x, y, False)
                    
                #ledm.led(x, y, False)
                #time.sleep(0.2)


if __name__ == "__main__":
    main()
