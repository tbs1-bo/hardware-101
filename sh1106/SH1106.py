# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# SH1106 edition of SH1106 (HW101)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import logging
import time

# Constants
SH1106_I2C_ADDRESS = 0x3C    # 011110+SA0+RW - 0x3C or 0x3D
SH1106_SETCONTRAST = 0x81
SH1106_DISPLAYALLON_RESUME = 0xA4
SH1106_DISPLAYALLON = 0xA5
SH1106_NORMALDISPLAY = 0xA6
SH1106_INVERTDISPLAY = 0xA7
SH1106_DISPLAYOFF = 0xAE
SH1106_DISPLAYON = 0xAF
SH1106_SETDISPLAYOFFSET = 0xD3
SH1106_SETCOMPINS = 0xDA
SH1106_SETVCOMDETECT = 0xDB
SH1106_SETDISPLAYCLOCKDIV = 0xD5
SH1106_SETPRECHARGE = 0xD9
SH1106_SETMULTIPLEX = 0xA8
SH1106_SETLOWCOLUMN = 0x00
SH1106_SETHIGHCOLUMN = 0x10
SH1106_SETSTARTLINE = 0x40
SH1106_SETPAGEADDR = 0xB0
SH1106_COMSCANINC = 0xC0
SH1106_COMSCANDEC = 0xC8
SH1106_SEGREMAP = 0xA0
SH1106_CHARGEPUMP = 0x8D
SH1106_EXTERNALVCC = 0x1
SH1106_SWITCHCAPVCC = 0x2

# Scrolling constants
SH1106_ACTIVATE_SCROLL = 0x2F
SH1106_DEACTIVATE_SCROLL = 0x2E
SH1106_SET_VERTICAL_SCROLL_AREA = 0xA3
SH1106_RIGHT_HORIZONTAL_SCROLL = 0x26
SH1106_LEFT_HORIZONTAL_SCROLL = 0x27
SH1106_VERTICAL_AND_RIGHT_HORIZONTAL_SCROLL = 0x29
SH1106_VERTICAL_AND_LEFT_HORIZONTAL_SCROLL = 0x2A


class SH1106Base(object):
    """Base class for SH1106-based OLED displays.  Implementors should subclass
    and provide an implementation for the _initialize function.
    """

    def __init__(self, width, height, rst=None, dc=None, sclk=None, din=None, cs=None,
                 gpio=None, spi=None, i2c_bus=None, i2c_address=SH1106_I2C_ADDRESS,
                 i2c=None):
        self._log = logging.getLogger('Adafruit_SH1106.SH1106Base')
        self._spi = None
        self._i2c = i2c #HW101
        self._i2c_address = i2c_address #HW101
        self.width = width
        self.height = height
        self._pages = height//8
        self._buffer = [0x00]*(width*self._pages)
        self._rst = rst
        self._gpio = gpio
        """
        # Default to platform GPIO if not provided.
        self._gpio = gpio
        if self._gpio is None:
            self._gpio = GPIO.get_platform_gpio()
        # Setup reset pin.
        self._rst = rst
        if not self._rst is None:
            self._gpio.setup(self._rst, GPIO.OUT)
        # Handle hardware SPI
        if spi is not None:
            self._log.debug('Using hardware SPI')
            self._spi = spi
            self._spi.set_clock_hz(8000000)
        # Handle software SPI
        elif sclk is not None and din is not None and cs is not None:
            self._log.debug('Using software SPI')
            self._spi = SPI.BitBang(self._gpio, sclk, din, None, cs)
        # Handle hardware I2C
        elif i2c is not None:
            self._log.debug('Using hardware I2C with custom I2C provider.')
            self._i2c = i2c.get_i2c_device(i2c_address)
        else:
            self._log.debug('Using hardware I2C with platform I2C provider.')
            import Adafruit_GPIO.I2C as I2C
            if i2c_bus is None:
                self._i2c = I2C.get_i2c_device(i2c_address)
            else:
                self._i2c = I2C.get_i2c_device(i2c_address, busnum=i2c_bus)
        # Initialize DC pin if using SPI.
        if self._spi is not None:
            if dc is None:
                raise ValueError('DC pin must be provided when using SPI.')
            self._dc = dc
            self._gpio.setup(self._dc, GPIO.OUT)
        """

    def _initialize(self):
        raise NotImplementedError

    def command(self, c):
        """Send command byte to display."""
        if self._spi is not None:
            # SPI write.
            self._gpio.set_low(self._dc)
            self._spi.write([c])
        else:
            # I2C write.
            control = 0x00   # Co = 0, DC = 0
            #self._i2c.write8(control, c)
            self._i2c.write_byte_data(self._i2c_address, control, c) #HW101

    def data(self, c):
        """Send byte of data to display."""
        if self._spi is not None:
            # SPI write.
            self._gpio.set_high(self._dc)
            self._spi.write([c])
        else:
            # I2C write.
            control = 0x40   # Co = 0, DC = 0
            #self._i2c.write8(control, c)
            self._i2c.write_byte_data(self._i2c_address, control, c) # HW101

    def begin(self, vccstate=SH1106_SWITCHCAPVCC):
        """Initialize display."""
        # Save vcc state.
        self._vccstate = vccstate
        # Reset and initialize display.
        self.reset()
        self._initialize()
        # Turn on the display.
        self.command(SH1106_DISPLAYON)

    def reset(self):
        """Reset the display."""
        if self._rst is None:
            return
        """
        # Set reset high for a millisecond.
        self._gpio.set_high(self._rst)
        time.sleep(0.001)
        # Set reset low for 10 milliseconds.
        self._gpio.set_low(self._rst)
        time.sleep(0.010)
        # Set reset high again.
        self._gpio.set_high(self._rst)
        """

    def display(self):
        """Write display buffer to physical display."""
        self.command(SH1106_SETSTARTLINE)
        self.command(0xD3)
        self.command(0x00)
        for p in range(8):
            self.command(SH1106_SETPAGEADDR|p)
            self.command(SH1106_SETLOWCOLUMN)
            self.command(SH1106_SETHIGHCOLUMN)
            for x in range(0,self.width,16):
                control = 0x40
                index = self.width*p + x
                self._i2c.write_i2c_block_data(SH1106_I2C_ADDRESS, control, self._buffer[index:index+16])


    def image(self, image):
        """Set buffer to value of Python Imaging Library image.  The image should
        be in 1 bit mode and a size equal to the display size.
        """
        if image.mode != '1':
            raise ValueError('Image must be in mode 1.')
        imwidth, imheight = image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display ({0}x{1}).' \
                .format(self.width, self.height))
        # Grab all the pixels from the image, faster than getpixel.
        pix = image.load()
        # Iterate through the memory pages
        index = 0
        for page in range(self._pages):
            # Iterate through all x axis columns.
            for x in range(self.width):
                # Set the bits for the column of pixels at the current position.
                bits = 0
                # Don't use range here as it's a bit slow
                for bit in [0, 1, 2, 3, 4, 5, 6, 7]:
                    bits = bits << 1
                    bits |= 0 if pix[(x, page*8+7-bit)] == 0 else 1
                # Update buffer byte and increment to next byte.
                self._buffer[index] = bits
                index += 1

    def clear(self):
        """Clear contents of image buffer."""
        self._buffer = [0x00]*(self.width*self._pages)

    def set_contrast(self, contrast):
        """Sets the contrast of the display.  Contrast should be a value between
        0 and 255."""
        if contrast < 0 or contrast > 255:
            raise ValueError('Contrast must be a value from 0 to 255 (inclusive).')
        self.command(SH1106_SETCONTRAST)
        self.command(contrast)

    def dim(self, dim):
        """Adjusts contrast to dim the display if dim is True, otherwise sets the
        contrast to normal brightness if dim is False.
        """
        # Assume dim display.
        contrast = 0
        # Adjust contrast based on VCC if not dimming.
        if not dim:
            if self._vccstate == SH1106_EXTERNALVCC:
                contrast = 0x9F
            else:
                contrast = 0xCF


class SH1106_128_64(SH1106Base):
    def __init__(self, rst=None, dc=None, sclk=None, din=None, cs=None, gpio=None,
                 spi=None, i2c_bus=None, i2c_address=SH1106_I2C_ADDRESS, i2c=None):
        # Call base class constructor.
        super(SH1106_128_64, self).__init__(128, 64, rst, dc, sclk, din, cs,
                                             gpio, spi, i2c_bus, i2c_address, i2c)

    def _initialize(self):
        print("test")
        # 128x64 pixel specific initialization.
        self.command(SH1106_DISPLAYOFF)                    # 0xAE
        self.command(SH1106_SETDISPLAYCLOCKDIV)            # 0xD5
        self.command(0x80)                                  # the suggested ratio 0x80
        self.command(SH1106_SETMULTIPLEX)                  # 0xA8
        self.command(0x3F)
        self.command(SH1106_CHARGEPUMP)                    # 0x8D
        #self.command(0xad)
        if self._vccstate == SH1106_EXTERNALVCC:
            self.command(0x10)
        else:
            self.command(0x14)
        self.command(SH1106_COMSCANDEC)
        self.command(SH1106_SETCOMPINS)                    # 0xDA
        self.command(0x12)
        self.command(SH1106_SETCONTRAST)                   # 0x81
        if self._vccstate == SH1106_EXTERNALVCC:
            self.command(0x9F)
        else:
            self.command(0xCF)
        self.command(SH1106_SETPRECHARGE)                  # 0xd9
        if self._vccstate == SH1106_EXTERNALVCC:
            self.command(0x22)
        else:
            self.command(0xF1)
            #self.command(0x1F)
        self.command(SH1106_SETVCOMDETECT)                 # 0xDB
        self.command(0x40)
        self.command(SH1106_DISPLAYALLON_RESUME)           # 0xA4
        self.command(SH1106_NORMALDISPLAY)                 # 0xA6

