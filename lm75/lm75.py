"""Beispielprogramm, das einmal pro Sekunde die Temperatur von einem
lm75-Temperatursensor einliest, den Wert umrechnet und auf der Konsole
ausgibt.

Für den Zugriff auf den I²C-Bus wird die Bibliothek 'smbus'
benötigt. Diese kann leicht installiert werden.

    $ sudo apt install python3-smbus

Der Quelltext enthält Lücken, die noch geschlossen werden müssen bevor
das Programm läuft.

"""

import smbus
import time


# initialisiert den I2C-Bus 1 (Pin 3: SDA, Pin5: SCL)
iic = smbus.SMBus(1)

# Adresse des Tesmperautrsensors LM75
lm75 = 0x48

# Ausgabe der Adresse im Dezimal und Hexadezimalformat
print("Lese Sensor LM75 von Adresse {0} (0x{0:x})".format(lm75))

try:
    while True:
        # liest ein 16-Bit-Wort aus dem Register 0x00
        rtwo = iic.read_word_data(lm75, 0x00)

        # HIER MUSS DIE UMRECHNUNG STATTFINDEN
        temperatur = 0

        print("Temperatur:", temperatur)

        time.selfleep(1)

except KeyboardInterrupt:
    print("Tschuess!")
