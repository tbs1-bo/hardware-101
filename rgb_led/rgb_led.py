from gpiozero import RGBLED
from time import sleep

# LED-Objekt wird mit drei BCM-Pins erstellt. Der vierte LED-Pin wird mit GND
# verbunden.
# https://gpiozero.readthedocs.io/en/stable/api_output.html?#gpiozero.RGBLED
#
led = RGBLED(red=2, green=3, blue=4)

# Einzelne Farbwerte können können über das color-Attribut gesetzt werden. Hier
# wird ein Wert zwischen 0 und 1 für jede Farbe rot, grün und blau genutzt.

print('LED rot')
led.color = (1, 0, 0)
sleep(1)

print('LED gelb')
led.color = (1, 1, 0)
sleep(1)

# Mit der colorzero Bibliothek kann zwischen verschiedenen Farbräumen 
# konvertiert werden. Für einen Regebogen bietet sich das HSV-Modell an.
# https://de.wikipedia.org/wiki/HSV-Farbraum

print('Regenbogen')
from colorzero import Color

for h in range(1, 101):
    col = Color.from_hsv(h/100, 1, 1)
    led.color = col
    sleep(0.1)

print('Ende')
sleep(1)
led.off()
