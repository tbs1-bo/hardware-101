import RPi.GPIO as GPIO
import time

# set pin for hardware PWM
SERVOPIN = 17
# set a frequency to be used by the servo (in Hz)
FREQUENCY = 50

# some default duty cycles
LEFT = 2
RIGHT = 12
CENTER = 8


class Servo:
    def __init__(self, servopin, dc_defaults,
                 boardmode=GPIO.BCM, frequency=50):
        """Create servo connected with frequency freq to pin. dc_defaults
        contains default duty cylces for values of left, center and
        right.
        """
        self.left, self.center, self.right = dc_defaults

        # first setup the pi
        GPIO.setmode(boardmode)
        GPIO.setup(servopin, GPIO.OUT)

        # creating pwm pin
        self.pwm = GPIO.PWM(servopin, frequency)
        self.pwm.start(0)

    def change_dc(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        self.pwm.stop()


def main():
    servo = Servo(servopin=SERVOPIN, dc_defaults=[LEFT, CENTER, RIGHT],
                  frequency=FREQUENCY)

    servo.change_dc(LEFT)
    time.sleep(2)
    servo.change(RIGHT)
    time.sleep(2)
    servo.change(CENTER)
    time.sleep(2)

    servo.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()


