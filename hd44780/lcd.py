import RPi.GPIO as GPIO
import time


class LCD:
    CLEAR_DISPLAY = 0x01
    RETURN_HOME = 0x02

    def __init__(self, e_pin, rs_pin, d4, d5, d6, d7, boardmode=GPIO.BCM):
        GPIO.setmode(boardmode)

        self.rs_pin = rs_pin
        self.e_pin = e_pin
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7

        # all pins are output pins
        GPIO.setup([rs_pin, e_pin, d4, d5, d6, d7],
                   GPIO.OUT)

    def tick(self, time_wait=0.001):
        """Make one clock cycle on the E pin."""

        GPIO.output(self.e_pin, GPIO.LOW)
        time.sleep(time_wait)
        GPIO.output(self.e_pin, GPIO.HIGH)
        time.sleep(time_wait)
        GPIO.output(self.e_pin, GPIO.LOW)

    def set_rs(self, signal):
        GPIO.output(self.rs_pin, signal)

    def send_data(self, byte, data_mode):
        """Send one byte on the pin connected to d4-d7. data_mode determines
        whether it should be send as instructions (=0) or data (=1)."""

        self.set_rs(data_mode)

        # creating array of truth values corresponding to set bits in
        # the byte
        hi = [(byte >> 4) & 1 > 0,
              (byte >> 5) & 1 > 0,
              (byte >> 6) & 1 > 0,
              (byte >> 7) & 1 > 0]

        lo = [(byte) & 1 > 0,
              (byte >> 1) & 1 > 0,
              (byte >> 2) & 1 > 0,
              (byte >> 3) & 1 > 0]

        # First: writing upper 4 bits
        GPIO.output([self.d4, self.d5, self.d6, self.d7], hi)
        self.tick()
        # Second: writing lower 4 bits
        GPIO.output([self.d4, self.d5, self.d6, self.d7], lo)
        self.tick()


if __name__ == "__main__":
    lcd = LCD(e_pin=10, rs_pin=25,
              d4=24, d5=23, d6=18, d7=17)

    # configure by "return home" instruction
    lcd.send_data(LCD.RETURN_HOME, 0)

    # clear display
    lcd.send_data(LCD.CLEAR_DISPLAY, 0)

    # send command
    lcd.send_data(ord("H"), 1)
    lcd.send_data(ord("i"), 1)

    GPIO.cleanup()
