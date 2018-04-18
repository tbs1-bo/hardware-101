import os


class DS18B20:
    def __init__(self, serialnr):
        # in this folder all devices are stored
        self.base_path = "/sys/devices/w1_bus_master1/"
        # this file contains the current value
        self.slave_file = "w1_slave"
        # family 0x28: DS18B20 temp sensor
        family = "28"
        # create device name from family and serial number
        self.device_name = family + "-" + serialnr

        self.sensorpath = os.path.join(self.base_path, self.device_name,
                                       self.slave_file)

        if not os.path.exists(self.sensorpath):
            raise Exception("Sensor not found at " + str(self.sensorpath))

    def read_raw_value(self):
        f = open(self.sensorpath, "r")
        lines = f.readlines()

        if "YES" not in lines[0]:
            raise Exception("Sensor not ready")

        temp_line = lines[1]
        val = temp_line.split("=")[1]
        return int(val)


if __name__ == "__main__":
    ds = DS18B20('0000064d724b')
    temp_raw = ds.read_raw_value()
    print("Temperature {temp} °C (raw: {raw})".format(temp=temp_raw / 1000,
                                                      raw=temp_raw))
