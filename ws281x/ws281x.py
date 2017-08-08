import time
import neopixel


# GPIO Daten pin (muss PWM unterstützen).
LED_PIN = 18

# LED Signal Frequenz in Hertz (normalerweise 800khz)
LED_FREQ_HZ = 800000

# DMA Kanal, um das Signal zu erzeugen (default 5)
LED_DMA = 5

# 0 für dunkle und 255 für helle LEDs.
LED_BRIGHTNESS = 255

# True, um das Signal zu invertieren (NPN Transistor für 3V->5V)
LED_INVERT = False

# Anzahl der LEDs auf dem Streifen
LED_COUNT = 8

strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                                   LED_INVERT, LED_BRIGHTNESS)
strip.begin()

color_red = neopixel.Color(255, 0, 0)
for i in range(strip.numPixels()):
    strip.setPixelColor(i, color_red)
    strip.show()
    time.sleep(0.5)
