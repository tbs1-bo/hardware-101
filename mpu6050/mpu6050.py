import smbus
import time
import math


class bmx055:
    def __init__(self):
        self.bus = smbus.SMBus(1)

    def read_Acceleration(self):
        self.bus.write_byte_data(0x18, 0x0F, 0x03)
        self.bus.write_byte_data(0x18, 0x10, 0x08)
        self.bus.write_byte_data(0x18, 0x11, 0x00)

        time.sleep(0.5)
        data = self.bus.read_i2c_block_data(0x18, 0x02, 6)

        xAccl = ((data[1] * 256) + (data[0] & 0xF0)) / 16
        if xAccl > 2047:
            xAccl -= 4096
        yAccl = ((data[3] * 256) + (data[2] & 0xF0)) / 16
        if yAccl > 2047:
            yAccl -= 4096
        zAccl = ((data[5] * 256) + (data[4] & 0xF0)) / 16
        if zAccl > 2047:
            zAccl -= 4096

        #print("Acceleration in X-Axis : %d" % xAccl)
        print("Acceleration in Y-Axis : %d" % yAccl)
        print("Acceleration in Z-Axis : %d" % zAccl)

        achsen = {"x": xAccl, "y": yAccl, "z": zAccl}
        return achsen

    def read_rotation(self):

        self.bus.write_byte_data(0x68, 0x0F, 0x04)
        self.bus.write_byte_data(0x68, 0x10, 0x07)
        self.bus.write_byte_data(0x68, 0x11, 0x00)

        time.sleep(0.5)

        data = self.bus.read_i2c_block_data(0x68, 0x02, 6)

        xGyro = data[1] * 256 + data[0]
        if xGyro > 32767:
            xGyro -= 65536
        yGyro = data[3] * 256 + data[2]
        if yGyro > 32767:
            yGyro -= 65536
        zGyro = data[5] * 256 + data[4]
        if zGyro > 32767:
            zGyro -= 65536

        print("X-Axis of Rotation : %d" % xGyro)
        print("Y-Axis of Rotation : %d" % yGyro)
        print("Z-Axis of Rotation : %d" % zGyro)

        achsen = {"x":xGyro, "y":yGyro, "z":zGyro}
        return achsen

    def read_magnetfeld(self):

        self.bus.write_byte_data(0x10, 0x4B, 0x83)
        self.bus.write_byte_data(0x10, 0x4C, 0x00)
        self.bus.write_byte_data(0x10, 0x4E, 0x84)
        self.bus.write_byte_data(0x10, 0x51, 0x04)
        self.bus.write_byte_data(0x10, 0x52, 0x0F)

        time.sleep(0.5)

        data = self.bus.read_i2c_block_data(0x10, 0x42, 6)

        xMag = ((data[1] * 256) + (data[0] & 0xF8)) / 8
        if xMag > 4095:
            xMag -= 8192
        yMag = ((data[3] * 256) + (data[2] & 0xF8)) / 8
        if yMag > 4095:
            yMag -= 8192
        zMag = ((data[5] * 256) + (data[4] & 0xFE)) / 2
        if zMag > 16383:
            zMag -= 32768

        print("Magnetic field in X-Axis : %d" % xMag)
        print("Magnetic field in Y-Axis : %d" % yMag)
        print("Magnetic field in Z-Axis : %d" % zMag)

        achsen = {"x": xMag, "y": yMag, "z": zMag}
        return achsen

class mpu6050:
    def __init__(self):
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
        a = mpu6050()
        test = a.get_xyz_rotation()
        print(test)
        test = a.get_xyz_beschleunigung()
        print(test)
