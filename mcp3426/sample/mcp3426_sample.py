import time
import smbus
import os

class MCP3426:
    def __init__(self, busnumber):
        assert busnumber in [0, 1]
        self.busnumber = busnumber
        self.slave_address = 0x68
        self.smbus = smbus.SMBus(1)

    def _swap_bytes(self, word):
        """ swap the two bytes of the given word
            example: word = 0xABCD -> return 0xCDAB """
        return ((word << 8) & 0xFF00) + (word >> 8)

    def _two_complement(self, word):
        """ convert the given word in two's complement to an integer with 
        sign """
        if (word >= 0x8000):
            return -((0xFFFF - word) + 1)
        else:
            return word

    def read_ch1(self):
        """ read the signal-value of channel 1 from the MCP3426
            and return the voltage in volt """
        rdwo = self.smbus.read_word_data(self.slave_address, 0x00)
        word = self._swap_bytes(rdwo)
        voltage = self._two_complement(word)
        return voltage / 1000
        return 1

def main():
    """ init ADC on I2C 1 """
    adc = MCP3426(1) 

    try: 
        while(True):
            ch1 = adc.read_ch1()              # voltage on channel 1 of the adc
            voltage = round(ch1 * 3, 2)       # operating voltage of the raspberry pi
            os.system("clear")                # clear screen
            print("Operating voltage of the Raspberry Pi:")
            print(voltage, "V")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()