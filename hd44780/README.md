LCD-Treiber HD44780 
===================

![lcd](doc/lcd.jpg)

Das C1602A ([Datenblatt](doc/C1602a.pdf)) ist ein Board, das ein
LC-Display und einen zugehörigen Treiber auf einer Platine vereint. Das
Display wird mit dem Treiber 
[HD44780](http://www.mikrocontroller.net/articles/HD44780)
angesteuert und in dem
[Datenblatt](doc/HD44780.pdf) beschrieben.

Neben der Beschreibung auf dieser Seite und einer Erklärung
bei [Wikipedia](https://de.wikipedia.org/wiki/HD44780), erläutert eine
[Anleitung von Adafruit](doc/drive-a-16x2-lcd-directly-with-a-raspberry-pi.pdf) die Verwendung des Displays.

Funktionsweise
--------------

Das Display besitzt 16 (manchmal auch nur 14) Pins, die in Reihe angeordnet 
sind und über die es angesteuert werden kann. 

- Pin 1 Vss: GND
- Pin 2 Vcc: Versorgungsspannung 5 Volt
- Pin 3 V0: Kontrastspannung, zwischen VEE und VCC, kann auf VSS
  gelegt oder via Poti angeschlossen werden. Auch eine Steurung über eine 
  PWM-Pin wäre möglich.
- Pin 4 RS: Registerauswahl (0 = Befehlsregister, 1 = Datenregister)
- Pin 5 R/W: Lese- oder Schreibzugriff; wird fest auf GND gelegt
  werden, damit keine 5V-Signale in den Pi gelangen.
- Pin 6 E: Taktleitung (Achtung! Diese Leitung hat im Gegensatz zu den
  anderen bei einigen Displays keinen internen Pullup, man muss also
  einen externen vorsehen.)
- Pin 7 DB0: Datenleitung (bleibt im 4-Bit-Modus offen)
- Pin 8 DB1: Datenleitung (bleibt im 4-Bit-Modus offen)
- Pin 9 DB2: Datenleitung (bleibt im 4-Bit-Modus offen)
- Pin 10 DB3: Datenleitung (bleibt im 4-Bit-Modus offen)
- Pin 11 DB4: Datenleitung
- Pin 12 DB5: Datenleitung
- Pin 13 DB6: Datenleitung
- Pin 14 DB7: Datenleitung
- Pin 15 A: Anode der LED-Hintergrundbeleuchtung (5V)
- Pin 16 K: Kathode der LED-Hintergrundbeleuchtung

Der RS-Pin bestimmt, ob ein Befehl oder Daten über die Pins DB0-7
gesendet werden. Die möglichen Befehle werden im Datenblatt im Abschnitt 
*Instructions* beschrieben. 

Pin E liefert ein Taktsignal. Bei steigender Flanke werden die Signale
auf den Pins DB0-7 als Befehl (RS=0) oder Daten (RS=1) interpretiert.

Zeichen für die Darstellung werden aus einem Character Generator ROM/RAM 
gelesen. Das RAM kann auch mit eigenen Zeichen beschrieben werden. Die
vorhandenen Zeichen befinden sich ebenfalls im Datenblatt.



Schaltung
---------

![schaltung_schema](doc/schaltung_schema.png)

![schaltung](doc/schaltung_Steckplatine.png)

![schaltung](doc/lcd_breadboard.jpg)

Das Display wird mit 5V betrieben. Da der Pi nur 3,3 V an seinen
Eingangspins verträgt, darf das Display nur beschrieben, nicht jedoch
ausgelesen werden. Daher ist Pin 5 (R/W) mit GND (0=Schreiben)
verbunden, um ein Lesen zu verhindern.


Quelltext
---------

Eine einfache Anzeige wird im Quelltext der Datei [lcd.py](lcd.py) realisiert.
Nachdem das Display initialisiert wurde, werden zwei Buchstaben an das Display
gesendet.

Die Bibliothek 
[Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD)
von Adafruit bietet einen leichteren Einstieg, wenn die Ansteuerung technisch
zu anspruchsvoll ist.


Funktionsprüfung
----------------

[![Youtube Demo Video](https://img.youtube.com/vi/W6sKhcwKmA4/0.jpg)](https://www.youtube-nocookie.com/embed/W6sKhcwKmA4?rel=0) 


Ein Video 
([mp4](https://archive.org/download/lcd_display_demo/MUTE_20170809_220636.mp4),
[ogg](https://archive.org/download/lcd_display_demo/MUTE_20170809_220636.ogv),
[YouTube](https://www.youtube-nocookie.com/embed/W6sKhcwKmA4?rel=0)) 
zeigt die Funktionsweise des Displays.


Links
-----

- [lcdproc](http://lcdproc.omnipotent.net/) zeigt Statusinformationen eines
  Linux-Servers auf einem Display an.
