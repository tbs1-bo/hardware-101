import RPi.GPIO as GPIO


class LCD:
    def __init__(self, rw_pin, db_pins):
        assert len(db_pins) == 4

        self.rw_pin = rw_pin
        self.db_pins = db_pins


if __name__ == "__main__":
    pass
