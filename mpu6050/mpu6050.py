import smbus
import time
import math


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
        h = self.i2c.read_byte_data(self.address, reg)
        l = self.i2c.read_byte_data(self.address, reg + 1)
        value = (h << 8) + l
        return value

    def read_word_2c(self, reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a, b):
        return math.sqrt((a * a) + (b * b))

    def get_y_rotation(self, x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return -math.degrees(radians)

    def get_x_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def get_xyz_rotation(self):
        gyro_xout = self.read_word_2c(self.regs["GYRO_XOUT_H"])
        # TODO: the same for the other coordinates
        gyro_yout = -1
        gyro_zout = -1

        # scaling the value realted to the sensitivity configured in FS_SEL
        # see section 4.19 in the register map document
        gyro_xout_scaled = gyro_xout / 131
        # TODO: the same for the other coordinates
        gyro_yout_scaled = -1
        gyro_zout_scaled = -1

        return {"x": [gyro_xout, gyro_xout_scaled],
                "y": [gyro_yout, gyro_yout_scaled],
                "z": [gyro_zout, gyro_zout_scaled]}


if "__main__" == __name__:
        a = MPU6050()
        while True:
            xyz_rot = a.get_xyz_rotation()
            print(xyz_rot)
            time.sleep(0.5)
