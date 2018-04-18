import machine

# GPIO0 (scl) und GPIO2 (sda) verwenden
# auf dem Board sind dies D3 und D4

i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2))
print(i2c.scan())
