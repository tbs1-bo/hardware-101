import time
import smbus

# Slaveadresse des MCP23017
IOEXP = 0x20
# Adressen der Register
IODIRA = 0x00   # Port A direction
IODIRB = 0x01   # Port B direction
GPIOA = 0x12    # Port A Werte
GPIOB = 0x13    # Port B Werte

# Initialisierung des I2C Bus
iic = smbus.SMBus(1)

# Konfiguration: Port B, Pin 0 als output
# 0xfe = 0b11111110
iic.write_byte_data(IOEXP, IODIRB, 0xfe)

try:
    while(True):
        # Port A lesen
        porta = iic.read_byte_data(IOEXP, GPIOA)
        # Pruefen, ob Port A, Pin 7 (Taster-Pin) gesetzt wurde
        # Registerinhalt mit 0x80 = 0b10000000 maskieren
        porta &= 0x80
        if porta  == 0x80:
            print("whoop")

        # Port B, Pin 0 (LED) einschalten
        # alle anderen Pins bleiben unveraendert
        portb = iic.read_byte_data(IOEXP, GPIOB)
        portb |= 0x01    # Verorderung mit 0x01
        iic.write_byte_data(IOEXP, GPIOB, portb)
        time.sleep(0.2)

        # Port B, Pin 0 ausschalten
        # alle anderen Pins bleiben unveraendern
        portb = iic.read_byte_data(IOEXP, GPIOB)
        portb &= ~0x01   # Verundung mit ~(0b00000001) = 0b11111110
        iic.write_byte_data(IOEXP, GPIOB, portb)
        time.sleep(0.2)
except KeyboardInterrupt:
    iic.close()
    print("Bye!")
