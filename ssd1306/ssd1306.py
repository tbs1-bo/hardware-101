import smbus
import time


class OLED:
    def __init__(self):
        self.I2CBUS = 1
        self.SLAVE_ADDRESS = 0x3C
        self.COMMAND_CONTROL_BYTE = 0x00  # to send commands
        self.DATA_CONTROL_BYTE = 0x40  # to send data
        self.OLED_ON = 0xAF
        self.OLED_OFF = 0xAE
        self.MUX_RATIO_COMMAND = 0xA8
        self.MUX_RATIO_VALUE = 0x3F  # 64MUX
        self.OFFSET_COMMAND = 0xD3
        self.OFFSET_VALUE = 0x00  # 0-63 (0x00-0x3F)
        self.START_LINE = 0x40 | 0x00  # 0-63 (0x40|0x00-0x40|0x3F)
        self.SEGMENT_REMAP = 0xA1  # or 0xA0
        self.COM_OUTPUT_SCAN_DIR = 0xC8  # or 0xC0
        self.COM_PINS_COMMAND = 0xDA
        self.COM_PINS_VALUE = 0x12  # or 0x02 or 0x22 or 0x32
        self.CONTRAST_COMMAND = 0x81
        self.CONTRAST_VALUE = 0xCF  # 1-256
        self.OLED_ALL_ON = 0xA5  # ignore RAM
        self.OLED_NOT_ALL_ON = 0xA4  # use the RAM
        self.OLED_INVERSE = 0xA7
        self.OLED_NOT_INVERSE = 0xA6  # normal
        self.CLOCK_DIV_COMMAND = 0xD5
        self.CLOCK_DIV_VALUE = 0x80
        self.CHARGE_PUMP_COMMAND = 0x8D
        self.CHARGE_PUMP_VALUE = 0x14  # to enable or 0x10 to disable
        self.ADDR_MODE_COMMAND = 0x20
        self.ADDR_MODE_VALUE = 0x00  # 0x00:horizontal 0x01:vertical 0x10:page

        self.i2c = smbus.SMBus(self.I2CBUS)
        self._config_oled()

    def _config_oled(self):
        """ Initialisation and configuration of SSD1306 for the
        128x64 OLED dot matrix."""
        # 00. Display Off AE
        self._send_command(self.OLED_OFF)
        # 01. Set MUX Ratio A8h, 3Fh
        self._send_command(self.MUX_RATIO_COMMAND)
        self._send_command(self.MUX_RATIO_VALUE)
        # 02. Set Display Offset D3h, 00h
        self._send_command(self.OFFSET_COMMAND)
        self._send_command(self.OFFSET_VALUE)
        # 03. Set Display Start Line 40h
        self._send_command(self.START_LINE)
        # 04. Set Segment re-map A0h/A1h
        self._send_command(self.SEGMENT_REMAP)
        # 05. Set COM Output Scan Direction C0h/C8h
        self._send_command(self.COM_OUTPUT_SCAN_DIR)
        # 06. Set COM Pins hardware configuration DAh, 02
        self._send_command(self.COM_PINS_COMMAND)
        self._send_command(self.COM_PINS_VALUE)
        # 07. Set Contrast Control 81h, 7Fh
        self._send_command(self.CONTRAST_COMMAND)
        self._send_command(self.CONTRAST_VALUE)
        # 08. Disable Entire Display On A4h
        self._send_command(self.OLED_NOT_ALL_ON)
        # 09. Set Normal Display A6h
        self._send_command(self.OLED_NOT_INVERSE)
        # 10. Set Osc Frequency D5h, 80h
        self._send_command(self.CLOCK_DIV_COMMAND)
        self._send_command(self.CLOCK_DIV_VALUE)
        # 11. Enable charge pump regulator 8Dh, 14h
        self._send_command(self.CHARGE_PUMP_COMMAND)
        self._send_command(self.CHARGE_PUMP_VALUE)
        # 12. Display On AFh
        self._send_command(self.OLED_ON)
        # some more configuration, maybe usefull
        # Memory Addressing Mode
        self._send_command(self.ADDR_MODE_COMMAND)
        self._send_command(self.ADDR_MODE_VALUE)
        # self._send_command(0xD9)    # 0xD9: set pre-charge period

        # 0xF1: value for pre-charge period
        # 0baaaabbbb: bbbb=phase1, aaaa=phase2, 1-5 DCLK (default 2)
        # self._send_command(0xF1)

        # self._send_command(0xDB)    # 0xDB: set V_COMH deselect level
        # self._send_command(0x40)    # 0x04: value for V_COMH (0x00 - 0x40)

    def _send_command(self, c):
        """ send a command to the SSD1306 (datasheet chapter 8.1.5)."""
        self.i2c.write_byte_data(self.SLAVE_ADDRESS,
                                 self.COMMAND_CONTROL_BYTE, c)

    def _send_data(self, d):
        """ send a data byte to the SSD1306."""
        self.i2c.write_byte_data(self.SLAVE_ADDRESS, self.DATA_CONTROL_BYTE, d)

    def _clear_display(self):
        """ send only zeros to the display.
            works only in horizontal or vertical mode."""
        for i in range(128 * 8):
            self._send_data(0x00)


def main():
    oled = OLED()
    oled._clear_display()
    while(True):
        for i in range(128 * 8):
            oled._send_data(0b11001100)
            time.sleep(0.005)
        time.sleep(2)
        for i in range(64):
            for j in range(8):
                oled._send_data(0b11110000)
            time.sleep(0.04)
            for j in range(8):
                oled._send_data(0b00001111)
            time.sleep(0.04)
        time.sleep(2)
        oled._send_command(oled.OLED_ALL_ON)
        time.sleep(1)
        oled._send_command(oled.OLED_NOT_ALL_ON)
        time.sleep(1)
        oled._send_command(oled.OLED_INVERSE)
        time.sleep(1)
        oled._send_command(oled.OLED_NOT_INVERSE)
        time.sleep(1)


if __name__ == "__main__":
    main()
