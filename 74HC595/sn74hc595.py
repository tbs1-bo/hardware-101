import RPi.GPIO as GPIO
import time


class SN74HC595:
    """
    A class that drives an 8Bit-shift register.

        ┌──◡──┐
    Qb  ┤1  16├ Vcc
    Qc  ┤2  15├ Qa
    Qd  ┤3  14├ SER
    Qe  ┤4  13├ ~OE
    Qf  ┤5  12├ RCLK
    Qg  ┤6  11├ SRCLK
    Qh  ┤7  10├ ~SRCLR
    GND ┤8   9├ Qh'
        └─────┘
    """

    def __init__(self, ser_pin, rclk_pin, srclk_pin, oe_pin,
                 clk_time=0.1, board_mode=GPIO.BCM):
        self.ser = ser_pin
        self.rclk = rclk_pin
        self.srclk = srclk_pin
        self.oe = oe_pin
        self.clk_time = clk_time

        GPIO.setmode(board_mode)
        # all pins are output pins
        for p in [self.ser, self.rclk, self.srclk, self.oe]:
            GPIO.setup(p, GPIO.OUT)

        self.output_enable(False)

    def tick_rclk(self):
        """One tick of the clock."""
        GPIO.output(self.rclk, GPIO.LOW)
        time.sleep(self.clk_time)
        GPIO.output(self.rclk, GPIO.HIGH)
        time.sleep(self.clk_time)

    def tick_srclk(self):
        """One tick of the clock."""
        GPIO.output(self.srclk, GPIO.LOW)
        time.sleep(self.clk_time)
        GPIO.output(self.srclk, GPIO.HIGH)
        time.sleep(self.clk_time)

    def output_enable(self, signal):
        GPIO.output(self.oe, not signal)

    def send_ser(self, signal):
        GPIO.output(self.ser, signal)


def main():
    register = SN74HC595(ser_pin=4, rclk_pin=18, srclk_pin=17, oe_pin=22,
                         clk_time=0.1)

    # enable the output
    register.output_enable(True)

    # send one bit into the register
    register.send_ser(True)
    # tick the clock
    register.tick_srclk()
    register.tick_rclk()
    # send another bit and tick again
    register.send_ser(False)
    register.tick_srclk()
    register.tick_rclk()

    # let the register tick some cycles
    for i in range(8):
        register.tick_srclk()
        register.tick_rclk()


if __name__ == "__main__":
    main()
