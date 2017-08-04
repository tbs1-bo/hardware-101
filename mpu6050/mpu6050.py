import smbus
import time
import math


class MPU6050:
    def __init__(self, address=0x68):
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c

        self.bus = smbus.SMBus(1)
        self.address = 0x68

        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

    def read_word(self, reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg + 1)
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
        gyroskop_xout = self.read_word_2c(0x43)
        gyroskop_yout = self.read_word_2c(0x45)
        gyroskop_zout = self.read_word_2c(0x47)

        gyroskop_xout_skaliert = gyroskop_xout / 131
        gyroskop_yout_skaliert = gyroskop_yout / 131
        gyroskop_zout_skaliert = gyroskop_zout / 131

        #print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", gyroskop_xout_skaliert)
        #print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", gyroskop_yout_skaliert)
        #print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", gyroskop_zout_skaliert)

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
