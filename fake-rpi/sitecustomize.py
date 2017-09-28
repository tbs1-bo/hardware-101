"""Module that will be imported before main.
https://stackoverflow.com/questions/32184440/making-python-run-a-few-lines-before-my-script
https://docs.python.org/3/library/site.html
"""

import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi
sys.modules['smbus'] = fake_rpi.smbus
