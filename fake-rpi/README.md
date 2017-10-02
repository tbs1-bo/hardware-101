# fake-rpi

Die Bibliothek
[fake-rpi](https://github.com/MomsFriendlyRobotCompany/fake_rpi) hilft
bei der Entwicklung von Programmen für den Raspberry Pi. Gewöhnlich
stehen manche Bibliotheken nämlich nur auf dem Pi selbst zur
Verfügung: etwa `RPi.GPIO` oder `smbus`. Sie können also nicht auf dem
Entwicklungsrechner genutzt werden und führen zu Programmabbrüchen.


## Verwendung mit Veränderung des Programmes

Nach der Installation mit `pip` kann die Bibliothek genutzt
werden. Hierfür kann der folgende Quelltext an den Anfang des
Programmes gesetzt werden. Es muss auf dem Pi wieder auskommentiert
werden. Alternativ könnte auch eine Variable über die Ausführung entscheiden.

    # Replace libraries by fake ones
    import sys
    import fake_rpi
    
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)


## Verwendung ohne Veränderung des Programmes

Alternativ kann die Datei [sitecustomize.py](sitecustomize.py) vor der
Ausführung in den Suchpfad aufgenommen werden. 
Diese Datei wird standardmäßig importiert und die Änderungen darin
werden für das folgende Programm wirksam.

Legt man sie neben das Programm in den gleichen Ordner, so
funktioniert der folgende Aufruf.

    $ PYTHONPATH=. python programm.py

