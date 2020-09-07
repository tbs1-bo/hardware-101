import spidev

class MCP23S17:
    def __init__(self, slave_address, busnumber, chipnumber):
        assert busnumber in [0, 1]
        assert chipnumber in [0, 1]
        self.controlbyte_write = slave_address<<1
        self.controlbyte_read = (slave_address<<1)+1
        self.spi = spidev.SpiDev()
        self.spi.open(busnumber, chipnumber)
        self.spi.max_speed_hz = 10000000
        # configure default registers
        self._regs = {'conf': {'A': 0x00, 'B': 0x01},
                      'input': {'A': 0x12, 'B': 0x13},
                      'output': {'A': 0x14, 'B': 0x15}}

    def write_config(self, portab, value):
        assert portab in ['A', 'B']
        reg = self._regs['conf'][portab]
        self.spi.xfer([self.controlbyte_write, reg, value])

    def read_config(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['conf'][portab]
        return self.spi.xfer([self.controlbyte_read, reg, 0])[2]

    def write_output(self, portab, value):
        assert portab in ['A', 'B']
        reg = self._regs['output'][portab]
        self.spi.xfer([self.controlbyte_write, reg, value])

    def read_output(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['output'][portab]
        return self.spi.xfer([self.controlbyte_read, reg, 0])[2]

    def read_input(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['input'][portab]
        return self.spi.xfer([self.controlbyte_read, reg, 0])[2]

