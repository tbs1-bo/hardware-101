Gertboard
=========

![Schaltbild](doc/gertboard_schaltbild.png)

Das Gertboard ist ein vielfältiges Erweiterungsboard für den Raspberry
Pi. Es vereint verschiedene Komponenten auf einer Platine. Eine
ausführliche Beschreibung befindet sich in dem
[Handbuch](doc/Gertboard_UM_with_python.pdf)
([deutsche Übersetzung](doc/Gertboard-Handbuch_deutsch.pdf)).
Die darin referenzierten Programme befinden sich in dem Archiv
[gertboard_py.zip](doc/gertboard_py.zip).

Funktionsblöcke
---------------

![Funktionsbloecke](doc/gertboard_funtional_blocks.png)

Die verschiedene Bestandteile des Gertboard sind im oberen Bild
farblich hervorgehoben.

* 12 gebufferte I/O Ports
* 3 Taster
* 6 open collector Treiber (50V, 0.5A)
* 1 Motortreiber (18V, 2A)
* 1 ATmega microcontroller (28-pin dual in line)
* 1 Digital-Analog Konverter (2 Kanäle: 8, 10, or 12 bit)
* 1 Analog-Digital Konverter (2 Kanäle: 10 bit)

LEDs und Buttons
----------------

Das Gertboard verfügt im oberen Bereich über zahlreiche LED und drei
Taster. Das Programm [gertboard-led_btn.py](gertboard-led_btn.py)
zeigt die Verwendung der Komponenten. Beim Drücken des Tasters wird
eine LED an und wieder ausgeschaltet.

Die beiden folgenden Bilder zeigen eine Verkabeling mit zwei
Steckbrücken und einem Jumper.

![led button](doc/gertboard_btn_led.jpg)

![schaltbild led btn](doc/gertboard_schaltbild_led_btn.png)

Hierfür werden die GPIO im unteren Bereich mit einem der Ports B1-B12
verbunden. Diese wiederum steuern die LED und Button an der oberen
Kante. Die Ports B1-B3 bedienen jeweils die Buttons.

Jeder der Ports ist wie folgt aufgebaut. Der hervorgehobene Bereich
ist nur bei den Taster-Ports B1-B3 vefügbar.

![ioport](doc/IOPort.png)

Der Jumper B5 (out) wurde gesetzt, um den Port B5 als Ausgang zu
deklarieren.

Digital-Analog Konverter
------------------------

Das Gertboard ist mit einem Digital-Analog-Konverter MCPx02
([Datenblatt](doc/mcp48x2.pdf)) bestückt, welches über SPI (Abschnitt
5 im Datenblatt) mit dem Gertboard und damit dem Pi kommuniziert.

Auf dem Gertboard kommen unterschiedliche Konverter mit einer
Auflösung von 8, 10 oder 12 Bit zum Einsatz. Welches Bauteil genau
verwendet wurde, lässt sich mit der Bauteilbeschriftung in U10 und dem
Handbuch ab Seite 32 klären.

Der Konnverter ist mit den Pins DA0 (Kanal 0) und DA1 (Kanal 1) in J29
verbunden. Er muss mit Jumpern in J11 und J2 wie folgt auf dem
Gertboard verdrahtet werden, um mittels SPI kommunizieren zu können.

              SCLK  MOSI  MISO     CS
    J11 ...o   o     o     o    o   o    o...
               |     |     |        |
    J2  ...o   o     o     o    o   o    o...
              GP11  GP10  GP09     GP07

Die analoge Ausgangsspannung ergibt sich bei einer Auflösug von 8-Bit
aus der Formel:

    Vout = (Din/256) * 2,084V

Für einen Test mit dem Programm [gertboard_da.py](gertboard_da.py)
wird ein Multimeter benötigt, das in J28 an DA0 angeschlossen wird.
