import smbus
from SH1106 import SH1106_128_64

# https://pillow.readthedocs.io/en/stable/
# PIL = Python Image Library kann mit pip als Paket pillow installiert werden.
#
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class OledDisplay(SH1106_128_64):
    def __init__(self, i2c:smbus.SMBus):
        super().__init__(i2c=i2c)
        self.image_data = Image.new('1', (self.width, self.height))
        self.image_draw = ImageDraw.Draw(self.image_data)
        self.font = ImageFont.load_default()
        
        self.begin()
    
    def draw_text(self, text, x, y):
        'Write the given text at position (x,y).'
        self.image_draw.text((x, y), text,  font=self.font, fill=255)

    def draw_line(self, x1, y1, x2, y2, width):
        'Draw a line with given width between (x1, y1) and (x2, y2).'
        self.image_draw.line([(x1,y1), (x2,y2)], fill=1, width=width)

    def draw_bitmap(self, x, y, imagefile):
        'Draw a bitmap loaded from a file at (x,y).'

        im = Image.open(imagefile)
        self.image_data.paste(im, box=(x,y))

    def px(self, x, y, value: bool):
        'Set or delete a pixel at (x,y).'
        f = 1 if value else 0
        self.image_draw.point((x,y), fill=f)

    def clear(self):
        super().clear()
        self.image_draw.rectangle(
            (0,0,self.width,self.height), 
            outline=0, fill=0)

    def display(self):
        'Write display buffer to the display.'
        self.image(self.image_data)
        super().display()

    def save_to_file(self, filename):
        'Save the current display buffer to a file.'

        self.image_data.save(filename)
