import spidev

class MCP3208:
    def __init__(self, busnumber, devicenumber, refvoltage):
        assert busnumber in [0, 1]
        assert devicenumber in [0, 1]
        self.spi = spidev.SpiDev()
        self.spi.open(busnumber, devicenumber)
        self.spi.max_speed_hz = 1000000
        self.refvoltage = refvoltage

    def read(self, channel):
        '''
        Three data bytes will be transmitted. The three channel bits CCC are encoded into 
        the first and second bytes in the following way.

        0000011C CCxxxxxx xxxxxxxx
        '''
        assert channel in range(8)
        data = self.spi.xfer([0b00000110 | (channel&0b100) >> 2, (channel&0b11)<<6, 0])
        value = (data[1] << 8) + data[2]
        voltage = self.refvoltage * value / 4096
        return voltage
