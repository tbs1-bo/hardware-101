from SH1106 import SH1106_128_64
import smbus

disp = SH1106_128_64(i2c=smbus.SMBus(1))
disp.begin()
disp.clear()
disp.display()
input()
for x in range(128*8):
    disp._buffer[x] = 0x00
for x in range(128):
    disp._buffer[128*(x%8) + x] = 0xFF
disp.display()
input()
for x in range(128*8):
    disp._buffer[x] = 0xFF
disp.display()
