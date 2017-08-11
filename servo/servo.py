import RPi.GPIO as GPIO
import time

# set pin for hardware PWM
servopin = 17
# set a frequency to be used by the servo (in Hz)
frequency = 50
# the pin numbering boardmode of the pi
boardmode = GPIO.BCM

# first setup the pi
GPIO.setmode(boardmode)
GPIO.setup(servopin, GPIO.OUT)

# creating pwm pin
pwm = GPIO.PWM(servopin, frequency)

print("Starting PWM")
pwm.start(2.5)
time.sleep(3)

# test different duty cycles
for dc in [3, 4, 5, 7, 9]:
    print("duty cycle:", dc)
    pwm.ChangeDutyCycle(dc)
    time.sleep(2)

pwm.stop()
GPIO.cleanup()
