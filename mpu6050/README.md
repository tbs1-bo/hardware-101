MPU6050 bzw. GY-521
===================

Der MPU 6050 ist ein Beschleunigungssensor, Temperatursensor und 
Gyrometer, der sich über I²C auslesen lässt. Er wird häufig auf 
einem breakout-board mit der Bezeichnung GY-521 geliefert.

Der IC wir in dem [Datenblatt des MPU6050](doc/mpu6050.pdf)
beschrieben. Eine ausführliche Beschreibung der zahlreichen Register
ist in dem separaten Dokument 
[MPU6050 Register Map](doc/MPU-6000-6050-Register-Map.pdf) verfügbar.


Schaltung
---------

![Schaltung](doc/schaltung_mpu6050_Steckplatine.png)

Der IC kann über den I²C-Bus direkt am Pi betrieben werden. Dort
meldet er sich unter der Adresse `0x68`. Zunächst muss der Chip aus
einem Schlafmodus erweckt werden, bevor die Sensordaten zur Verfügung
stehen.

Quelltext
---------

Ein Beispielprogramm befindet sich in der Datei [mpu6050.py](mpu6050.py). 
Es stellt eine Klasse `MPU6050` bereit, die die X-Achse des
Gyrosensors ausliest und einfach erweitert werden kann.


Links
-----

- [Anleitung für den Arduino](http://playground.arduino.cc/Main/MPU-6050)
