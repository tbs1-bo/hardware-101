# SPI controller is part of package python3-spidev
import spidev


class DAConverter:

    # configuring the DAC
    # bit 15 = channel, bit 14 = ignored, bit 13 =gain, bit 12 = shutdown,
    # bits 11-4 data, bits 3-0 ignored
    #
    # select channel of the DAC
    B_NOTA = 0b10000000
    NOT_GAIN = 0b00100000
    NOT_SHUTDOWN = 0b00010000

    def __init__(self, spi_bus, spi_dev):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_dev)

        # apply default settings
        #
        # using channel a
        self.b_nota = DAConverter.B_NOTA & 0
        # use no gain
        self.not_gain = DAConverter.NOT_GAIN & 0xFF
        # don't shutdown
        self.shutdown = DAConverter.NOT_GAIN & 0xFF

    def write_digital(self, value):
        """Write the given value to the bus. apply configurtion first"""

        b1 = self.B_NOTA | self.NOT_GAIN | self.NOT_SHUTDOWN
        # attach four bits of value to b1
        b1 = b1 | (value >> 4)
        # remaining bits for b2
        b2 = value << 4
        self.spi.xfer2([b1, b2])


def main():
    # some sample values that should be converted into analog output
    values = [1, 20, 50, 127, 255]
    dac = DAConverter(spi_bus=0, spi_dev=1)

    for v in values:
        print("value", v, end="\t")
        dac.write_digital(v)
        input("(Enter for next val)")

if __name__ == "__main__":
    main()
