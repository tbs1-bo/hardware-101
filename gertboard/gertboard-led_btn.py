import RPi.GPIO as GPIO
import time

led_pin = 25
btn_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_on = True
GPIO.output(led_pin, GPIO.HIGH)
time.sleep(1)

while True:
    # ask for negated input since pullup is active
    if not GPIO.input(btn_pin):
        print("Button pressed")
        led_on = not led_on
        GPIO.output(led_pin, led_on)
        print("led_on", led_on)
        time.sleep(0.5)
