import RPi.GPIO as GPIO
import time

led_pin = 25
btn_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN)

led_on = False
while True:
    if GPIO.input(btn_pin):
        print("Button pressed")
        led_on = not led_on
        GPIO.output(led_pin, led_on)
        time.sleep(0.01)
