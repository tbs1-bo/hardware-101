# SPI controller is part of package python3-spidev
import spidev


class DAConverter:

    # configuring the DAC
    #
    # bit 15 = channel (~A/B)
    B_NOTA = 0b10000000
    # bit 14 = ignored
    # bit 13 = gain
    NOT_GAIN = 0b00100000
    # bit 12 = shutdown
    NOT_SHUTDOWN = 0b00010000
    # bits 11-4 data (for 8 Bit)
    # bits 3-0 ignored or used for 10 or 12 Bit converters

    def __init__(self, spi_bus, spi_dev_select):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_dev_select)

        # apply default settings
        #
        # using channel a
        self.b_nota = DAConverter.B_NOTA & 0
        # use no gain
        self.not_gain = DAConverter.NOT_GAIN & 0xFF
        # don't shutdown
        self.shutdown = DAConverter.NOT_GAIN & 0xFF

    def write_digital(self, value):
        """Write the given value to the bus. apply configurtion first."""
        assert 0 <= value < 2**12, "Maximum of 12 Bits allowed."

        b1 = self.B_NOTA | self.NOT_GAIN | self.NOT_SHUTDOWN
        # attach four bits of value to b1
        b1 = b1 | (value >> 4)
        # remaining bits for b2
        b2 = value << 4

        self.spi.xfer2([b1, b2])


def main():
    # some sample values that should be converted into analog output
    values = [1, 20, 50, 127, 255]
    dac = DAConverter(spi_bus=0, spi_dev_select=1)

    for v in values:
        print("value", v, end="\t")
        dac.write_digital(v)
        input("(Enter for next val)")


if __name__ == "__main__":
    main()
