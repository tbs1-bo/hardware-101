import RPi.GPIO as GPIO
import time


class LCD:
    CLEAR_DISPLAY = 1
    RETURN_HOME = 2
    
    def __init__(self, e_pin, rs_pin, db_pins, boardmode=GPIO.BCM):
        assert len(db_pins) == 4

        GPIO.setmode(boardmode)
        
        self.rs_pin = rs_pin
        GPIO.setup(self.rs_pin, GPIO.OUT)
        self.e_pin = e_pin
        GPIO.setup(self.e_pin, GPIO.OUT)
        
        self.db_pins = db_pins

        GPIO.setup(self.rs_pin, GPIO.OUT)
        for p in self.db_pins:
            GPIO.setup(p, GPIO.OUT)

    def tick(self, time_wait=0.001):
        GPIO.output(self.e_pin, GPIO.LOW)
        time.sleep(time_wait)
        GPIO.output(self.e_pin, GPIO.HIGH)
        time.sleep(time_wait)
        GPIO.output(self.e_pin, GPIO.LOW)

    def set_rs(self, signal):
        GPIO.output(self.rs_pin, signal)

    def send_data(self, byte, data_mode):
        self.set_rs(data_mode)
        
        lo = [byte & 1 > 0,
              (byte >> 1) & 1 > 0,
              (byte >> 2) & 1 > 0,
              (byte >> 3) & 1 > 0]
        
        hi = [(byte >> 4) & 1 > 0,
              (byte >> 5) & 1 > 0,
              (byte >> 6) & 1 > 0,
              (byte >> 7) & 1 > 0]
        
        print("sending hi", hi, "lo", lo, "byte", byte)
        GPIO.output(self.db_pins, hi)
        self.tick()
        GPIO.output(self.db_pins, lo)
        self.tick()

    def _wait_ms(self, ms):
        end = time.time() + (ms/10000)
        while time.time() < end:
            pass


if __name__ == "__main__":
    lcd = LCD(e_pin=10, rs_pin=25,
              db_pins=[24, 23, 18, 17])

    # initialize display
    lcd.send_data(0x32, 0)
    lcd.send_data(0x33, 0)
    # send command
    #lcd.send_data(LCD.CLEAR_DISPLAY, 0)
    #lcd.send_data(LCD.RETURN_HOME, 0)    
    lcd.send_data(ord("H"), 1)
    lcd.send_data(ord("i"), 1)
    
    GPIO.cleanup()
    
