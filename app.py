import board
from time import sleep

import neopixel
from flask import Flask

app = Flask(__name__)

R = 255
G = 180
B = 100
BRIGHTNESS = 0.15

def refresh_tree():
    pixels = neopixel.NeoPixel(board.D21, 100, brightness=BRIGHTNESS)
    pixels.fill((0,0,0))
    sleep(1)
    pixels.fill((G,R,B))
    pixels.show()

@app.route('/brightness/<float:brightness>')
def set_brightness(brightness):
    if 0 <= brightness <= 1:
        global BRIGHTNESS
        BRIGHTNESS = brightness
        refresh_tree()
        return 'ok'
    else:
        return 'brightness not in [0, 1]', 400

@app.route('/colour/<int:r>/<int:g>/<int:b>')
def set_colour(r, g, b):
    if 0 <= r <= 255 and 0 <= g <=255 and 0 <= b <= 255:
        global R, G, B
        R, G, B = r, g, b
        refresh_tree()
        return 'ok'
    else:
        return 'r,b,g not in range [0, 255]', 400
