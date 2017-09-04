import time
import smbus

# Slaveadresse des MCP23017
IOEXP = 0x20
# Adressen der Register
IODIRA = 0x00   # Port A direction
IODIRB = 0x01   # Port B direction
GPIOA = 0x12    # Port A input
GPIOB = 0x13    # Port B input
OLATA = 0x14    # Port A output
OLATB = 0x15    # Port B output

# Initialisierung des I2C Bus
iic = smbus.SMBus(1)

# Konfiguration: Port B, Pin 0 als output
# 0xFE = 0b11111110
iic.write_byte_data(IOEXP, IODIRB, 0xFE)

try:
    while(True):
        # Port A lesen
        porta = iic.read_byte_data(IOEXP, GPIOA)
        # Pruefen, ob Port A, Pin 7 (Taster-Pin) gesetzt wurde
        # Registerinhalt mit 0x80 = 0b10000000 maskieren
        porta &= 0x80
        if porta == 0x80:
            print("Taster wurde gedrückt!")

        # Port B, Pin 0 (LED) einschalten
        # alle anderen Pins bleiben unveraendert
        portb = iic.read_byte_data(IOEXP, OLATB)
        portb |= 0x01    # Veroderung mit 0x01
        iic.write_byte_data(IOEXP, OLATB, portb)
        time.sleep(0.2)

        # Port B, Pin 0 ausschalten
        # alle anderen Pins bleiben unverändert
        portb = iic.read_byte_data(IOEXP, OLATB)
        portb &= ~0x01   # Verundung mit ~(0b00000001) = 0b11111110
        iic.write_byte_data(IOEXP, OLATB, portb)
        time.sleep(0.2)
except KeyboardInterrupt:
    iic.close()
    print("Bye!")
