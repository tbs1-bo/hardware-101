LED-Matrix (5x7)
==============

![LED-Matrix](doc/ledmatrix.png)

Die Matrix besteht aus einzelnen LEDs, die zeilen- und spaltenweise
miteinander verbunden sind. Damit lässt sich Jede LED aus einer
Kombination von Spalte und Zeile direkt ansteuern. Insgesamt werden
5+7=12 GPIO für die Ansteuerung benötigt.

Die LEDs werden mit einem Vorwiderstand von 220 Ohm betrieben. 

Anschluss (unvollständig)
---------

![Schaltung](doc/schaltung_Steckplatine.png)

Das Bild zeigt eine unvollständige Anschlussmöglichkeit, mit der die
vier LEDs im linken oberen Bereich angesteuert werden können.


Ansteuerung
-----------

Ein Beispielprogramm zur Ansteuerung der Matrix befindet sich in der
Datei [ledmatrix.py](ledmatrix.py). 

[![Demo Video](https://img.youtube.com/vi/pf3Cuj75bP4/0.jpg)](https://peertube.fidonet.io/videos/embed/8551bba8-45b9-40be-b55c-99e979b12471) 

Ein Video
[hier](https://youtu.be/pf3Cuj75bP4) oder 
[hier](https://archive.org/details/led_matrix_demo) zeigt die Matrix 
in Betrieb.

Datenblatt
----------

Die LED-Matrix ist vergleichbar mit der TC07-11 von Kingbright. 
- [Datenblatt](doc/TA07-11_TC07-11_datasheet.pdf)

Weitere Informationen
---------------------

Ein [Artikel bei 
mikrocontroller.net](https://www.mikrocontroller.net/articles/LED-Matrix) 
beschreibt LED-Matrizen genauer und geht auf unterschiedliche Möglichkeiten
der Ansteuerung ein. Ein 
[LED shield](https://wiki.wemos.cc/products:d1_mini_shields:matrix_led_shield)
für den Wemos D1 Mini enthält einen Controller für I²C-Display und vereinfacht
damit die Ansteuerung etwas. Die Ansteuerung noch größerer Displays beschreibt
Henner Zeller in dem Projekt
[rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix).
