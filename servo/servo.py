import RPi.GPIO as GPIO
import time

# set pin for hardware PWM
servopin = 17
frequency = 50  # Hz

boardmode = GPIO.BCM

GPIO.setmode(boardmode)
GPIO.setup(servopin, GPIO.OUT)

# using creating pwm pin
pwm = GPIO.PWM(servopin, frequency)

print("Starting PWM")
pwm.start(2.5)
time.sleep(3)

# test different duty cycles
for d in [3, 4, 5, 7, 9]:
    print("duty cycle:", d)
    pwm.ChangeDutyCycle(d)
    time.sleep(3)

pwm.stop()
GPIO.cleanup()
