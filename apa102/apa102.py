import spidev


# Anzahl der LEDs auf dem Streifen
LED_ANZAHL = 5

# Helligkeit von 0 bis 31
LED_HELLIGKEIT = 31

# SPI Port (normalerweise 1)
SPI_BUS = 0  # SPI port 0

# Slave Device (CS) 1
SPI_DEVICE = 1

# Taktfrequenz
SPI_FREQ_HZ = 8000000


if __name__ == "__main__":
    spi = spidev.SpiDev()
    spi.open(SPI_BUS, SPI_DEVICE)
    spi.max_speed_hz = SPI_FREQ_HZ

    # Start Frame => 32 Füllbits
    spi.xfer2([0] * 4)

    for i in range(LED_ANZAHL):
        # Helligkeit Byte setzten
        helligkeit = (LED_HELLIGKEIT & 0b00011111) | 0b11100000
        # Senden:  Helligkeit  Blau Grün Rot
        spi.xfer2([helligkeit, 255, 128, 0])

    # End Frame => 32 Endbits
    spi.xfer2([0] * 4)
    spi.close()
