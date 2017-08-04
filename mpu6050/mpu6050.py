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
        gyroskop_xout = self.read_word_2c(self.regs["GYRO_XOUT_H"])
        # TODO: the same for the other coordinates
        gyroskop_yout = -1
        gyroskop_zout = -1

        gyroskop_xout_skaliert = gyroskop_xout / 131
        # TODO: the same for the other coordinates
        gyroskop_yout_skaliert = -1
        gyroskop_zout_skaliert = -1

        return {"x": [gyroskop_xout, gyroskop_xout_skaliert],
                "y": [gyroskop_yout, gyroskop_yout_skaliert],
                "z": [gyroskop_zout, gyroskop_zout_skaliert]}

    def get_xyz_beschleunigung(self):
        beschleunigung_xout = self.read_word_2c(0x3b)
        beschleunigung_yout = self.read_word_2c(0x3d)
        beschleunigung_zout = self.read_word_2c(0x3f)

        beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
        beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
        beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0

        #print("beschleunigung_xout: ", ("%6d" % beschleunigung_xout),
        #       " skaliert: ", beschleunigung_xout_skaliert)
        #print("beschleunigung_yout: ", ("%6d" % beschleunigung_yout),
        #       " skaliert: ", beschleunigung_yout_skaliert)
        #print("beschleunigung_zout: ", ("%6d" % beschleunigung_zout),
        #       " skaliert: ", beschleunigung_zout_skaliert)

        x_rotation = self.get_x_rotation(beschleunigung_xout_skaliert,
            beschleunigung_yout_skaliert, beschleunigung_zout_skaliert)
        y_rotation = self.get_y_rotation(beschleunigung_xout_skaliert,
            beschleunigung_yout_skaliert, beschleunigung_zout_skaliert)

        #print("X Rotation: ", x_rotation)
        #print("Y Rotation: ", y_rotation)

        return {"x": [beschleunigung_xout, beschleunigung_xout_skaliert],
                "y": [beschleunigung_yout, beschleunigung_yout_skaliert],
                "z": [beschleunigung_zout, beschleunigung_zout_skaliert],
                "xrotation": x_rotation,
                "yrotation": y_rotation}


if "__main__" == __name__:
        a = MPU6050()
        while True:
            test = a.get_xyz_rotation()
            print(test)
            # test = a.get_xyz_beschleunigung()
            print(test)
            time.sleep(0.5)
