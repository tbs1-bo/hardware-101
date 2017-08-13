# SPI controller is part of package python3-spidev
import spidev

# SPI channel to be used
channel = 0
# SPI bus and devive
spi_bus, spi_dev = 0, 1

# some sample values that should be converted into analog output
values = [1, 20, 50, 127, 255]

spi = spidev.SpiDev()
spi.open(spi_bus, spi_dev)

for v in values:
    print("Value", v, end="\t")
    spi.xfer2([v, 0])
    input("(Enter for next value)")

r = spi.xfer2([16, 0])   # switch off channel A = 00010000 00000000 [16,0]
r = spi.xfer2([144, 0])  # switch off channel B = 10010000 00000000 [144,0]

# The DAC is controlled by writing 2 bytes (16 bits) to it.
# So we need to write a 16 bit word to DAC

# bit 15 = channel, bit 14 = ignored, bit 13 =gain, bit 12 = shutdown,
# bits 11-4 data, bits 3-0 ignored

# You feed spidev a decimal number and it converts it to 8 bit binary
# each argument is a byte (8 bits), so we need two arguments, which
# together make 16 bits.
