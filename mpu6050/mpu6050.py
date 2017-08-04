import smbus
import time


class MPU6050:
    def __init__(self, i2c_address=0x68):
        # Registers as described in the register map document (section 3)
        self.regs = {"POWER_MGM1_1": 0x6b,
                     "TEMP_OUT_H": 0x41,
                     "TEMP_OUT_L": 0x42,
                     "GYRO_XOUT_H": 0x43,  # described in section 4.19
                     "GYRO_XOUT_L": 0x44}  # ... and more

        self.i2c = smbus.SMBus(1)
        self.address = i2c_address

        # writing to register power_mgmt awakes the chip after powerup
        self.i2c.write_byte_data(self.address, self.regs["POWER_MGMT_1"], 0)

    def read_word(self, reg):
        """Read a word (2 Bytes) from a register."""
        h = self.i2c.read_byte_data(self.address, reg)
        l = self.i2c.read_byte_data(self.address, reg + 1)
        value = (h << 8) + l
        return value

    def read_word_2c(self, reg):
        """Read a word in 2-complement."""

        val = self.read_word(reg)

        if (val >= 0x8000):
            return -((0xFFFF - val) + 1)
        else:
            return val

    def get_xyz_rotation(self):
        gyro_xout = self.read_word_2c(self.regs["GYRO_XOUT_H"])
        # TODO: the same for the other axis y and z.
        # gyro_yout = ...
        # gyro_zout = ...

        # scaling the value relative to the sensitivity value configured in
        # register FS_SEL see section 4.4 and 4.19 in the register map document
        gyro_xout_scaled = gyro_xout / 131
        # TODO: the same for the other coordinates
        # gyro_yout_scaled = ...
        # gyro_zout_scaled = ...

        return {"x": [gyro_xout, gyro_xout_scaled],
                "y": "change this",
                "z": "change this"}


if "__main__" == __name__:
        a = MPU6050()
        while True:
            xyz_rot = a.get_xyz_rotation()
            print(xyz_rot)
            time.sleep(0.5)
