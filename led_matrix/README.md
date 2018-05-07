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

[![Youtube Demo Video](https://img.youtube.com/vi/pf3Cuj75bP4/0.jpg)](https://www.youtube-nocookie.com/embed/pf3Cuj75bP4?rel=0) 

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
