import time
import spidev

# Slaveadresse des MCP23S17
# IOEXP = 0x20
SPIBUS = 0    # SPI0
SPIDEVICE = 0 # CE0
IOEXPw = 0b01000000 # Opcode write
IOEXPr = 0b01000001 # Opcode read

# Adressen der Register
IODIRA = 0x00   # Port A direction
IODIRB = 0x01   # Port B direction
GPIOA = 0x12    # Port A input
GPIOB = 0x13    # Port B input
OLATA = 0x14    # Port A output
OLATB = 0x15    # Port B output

# Initialisierung des SPI Bus
spi = spidev.SpiDev()
spi.open(SPIBUS, SPIDEVICE)

# Konfiguration: Port A, Pin 0 als output
# 0xFE = 0b11111110
spi.xfer([IOEXPw, IODIRA, 0xFE])

try:
    while(True):
        # Port B lesen, Registerinhalt im dritten Byte
        portb = spi.xfer([IOEXPr, GPIOB, 0])[2]
        # Pruefen, ob Port B, Pin 0 (Taster-Pin) gesetzt wurde
        # Registerinhalt mit 0x01 = 0b00000001 maskieren
        portb = spi.xfer([IOEXPr, GPIOB, 0])[2]
        portb &= 0x01
        if portb == 0x01:
            print("whoop")

        # Port A, Pin 0 (LED) einschalten
        # alle anderen Pins bleiben unveraendert
        porta = spi.xfer([IOEXPr, OLATA, 0])[2]
        porta |= 0x01    # Veroderung mit 0x01
        spi.xfer([IOEXPw, OLATA, porta])
        time.sleep(0.2)

        # Port A, Pin 0 ausschalten
        # alle anderen Pins bleiben unveraendern
        porta = spi.xfer([IOEXPr, OLATA, 0])[2]
        porta &= ~0x01   # Verundung mit ~(0b00000001) = 0b11111110
        spi.xfer([IOEXPw, OLATA, porta])
        time.sleep(0.2)
except KeyboardInterrupt:
    spi.close()
    print("Bye!")
