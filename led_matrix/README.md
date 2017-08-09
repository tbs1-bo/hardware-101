LED-Matrix (5x7)
==============

![Bild](https://archive.org/download/led_matrix_demo/led_matrix_demo.thumbs/MUTE_20170803_085403_000001.jpg)
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

![Bild](https://archive.org/download/led_matrix_demo/led_matrix_demo.thumbs/MUTE_20170803_085403_000001.jpg)

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
der Ansteuerung ein.
