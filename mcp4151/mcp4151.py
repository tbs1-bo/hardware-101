import spidev

class MCP4151:
    def __init__(self, busnumber, devicenumber, speed_MHz=60):
        assert busnumber in [0, 1]
        assert devicenumber in [0, 1]
        self.spi = spidev.SpiDev()
        self.spi.open(busnumber, devicenumber)
        self.speed_Hz = speed_MHz * 1000000
        self.spi.max_speed_hz = speed_MHz * 1000000

    def set_wiper(self, value):
        assert value in range(257)
        self.spi.xfer([0x00 + value // 256, value % 256], self.speed_Hz, 0)

    def inc_wiper(self):
        self.spi.xfer([0b00000100], self.speed_Hz, 0)

    def dec_wiper(self):
        self.spi.xfer([0b00001000], self.speed_Hz, 0)
