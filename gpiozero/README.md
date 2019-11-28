# gpiozero

Die GPIO-Pins des Raspberry Pi können mit unterschiedlichen Bibliotheken gesteuert
und ausgelesen werden. Neben der Bibliothek mit dem Namen GPIO existiert in der
Standardinstallation des Pi auch die Bibliothek 
[gpiozero](https://gpiozero.readthedocs.io/).

## LED blinken lassen

Um die Klassen aus der Bibliothek nutzen zu können, müssen sie zunächst importiert
werden. Zunächst wird die LED-Klasse importiert. Da zwischen dem Ein-
und Ausschalten eine Weile vergehen soll, wird mit sleep eine Funktion zum Pausieren
des Programms zusätzlich importiert.


```python
from gpiozero import LED
from time import sleep
```

Nun wird ein Objekt der Klasse LED erzeugt. 

```pyhon
led = LED(17)
```

Der Name vor dem Gleichheitszeichen kann
frei gewählt werden. In ihr wird das neue LED-Objekt gespeichert. 

Mit der 17 wird der Pin angegeben, an dem die LED angeschlossen ist. Hier gibt es
verschiedene Arten der Zählweise. Wenn die Zahl direkt angegeben wird, ist die 
BCM-Nummerierung gemeint - also die Nummer des Pins direkt am Prozessor des Pi.
Diese unterscheidet sich von der physikalischen Board-Zählweise, bei die Pins
an der Pfostenleiste abgezählt werden.

Die LED kann auch mit der Board-Nummerierung erzeugt werden, wenn die
LED wie folgt erzeugt wird.

```pyhon
led = LED("BOARD11")
```

Nun wird der physikalische Pin Nummer 11 genutzt, der mit dem Pin 17
am Prozessor des Pi verbunden ist.

Das erstellte LED-Objekt hat verschiedene Methoden, die auf ihm
aufgerufen werden können. Wir nutzen die Methoden on() und off(), um
die LED ein- und ausschalten zu können.


```pyhon
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```
