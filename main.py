#!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky import InkyPHAT, InkyWHAT
from tautulli_graph import play_count_graph
from config import colour
# config
mounted_upside_down = True
strips = 5

# Setup objects
inky_display = InkyPHAT(colour)
play_count_graph()
img = Image.open("images/play_count.png")
gray = img.convert('L')
img = gray.point(lambda x: 255 if x<128 else 0, '1')

if mounted_upside_down:
    img = img.transpose(Image.ROTATE_180)
img = img.resize((inky_display.WIDTH, inky_display.HEIGHT))
inky_display.set_image(img)
inky_display.show()
