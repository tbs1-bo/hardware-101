import smbus

class MCP23017:
    def __init__(self, i2c_address, busnumber):
        assert busnumber in [0, 1]
        self.i2c_address = i2c_address
        self.smbus = smbus.SMBus(busnumber)
        # configure default registers
        self._regs = {'conf': {'A': 0x00, 'B': 0x01},
                      'input': {'A': 0x12, 'B': 0x13},
                      'output': {'A': 0x14, 'B': 0x15}}

    def write_config(self, portab, value):
        assert portab in ['A', 'B']
        reg = self._regs['conf'][portab]
        self.smbus.write_byte_data(self.i2c_address, reg, value)

    def read_config(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['conf'][portab]
        return self.smbus.read_byte_data(self.i2c_address, reg)

    def write_output(self, portab, value):
        assert portab in ['A', 'B']
        reg = self._regs['output'][portab]
        self.smbus.write_byte_data(self.i2c_address, reg, value)

    def read_output(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['output'][portab]
        return self.smbus.read_byte_data(self.i2c_address, reg)

    def read_input(self, portab):
        assert portab in ['A', 'B']
        reg = self._regs['input'][portab]
        return self.smbus.read_byte_data(self.i2c_address, reg)

