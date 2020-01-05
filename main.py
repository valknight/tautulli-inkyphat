#!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw
from font_intuitive import Intuitive
from inky import InkyPHAT, InkyWHAT
from tautulli_graph import play_count_graph
from config import colour, mounted_upside_down, show_text, days_to_show

# Setup objects
inky_display = InkyPHAT(colour)
play_count_graph(days=days_to_show)
img = Image.open("images/play_count.png")
img = img.convert('L')
img = img.point(lambda x: 255 if x < 240 else 0, '1')
img = img.resize((inky_display.WIDTH, inky_display.HEIGHT))

if show_text:
    # Put title text on Pi
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Intuitive, 22)

    message = "Plex Activity"
    w, h = font.getsize(message)
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = 0
    draw.text((x, y), message, inky_display.BLACK, font)

if mounted_upside_down:
    img = img.transpose(Image.ROTATE_180)
img.save("images/shown_graph.png", "PNG")
inky_display.set_image(img)
inky_display.show()
