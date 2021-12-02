import board
from time import sleep

import neopixel
from flask import Flask

app = Flask(__name__)

r = 255
g = 180
b = 100

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/brightness/<float:brightness>')
def set_brightness(brightness):
    if 0 <= brightness <= 1:
        pixels = neopixel.NeoPixel(board.D21, 100, brightness=brightness)
        pixels.fill((0,0,0))
        sleep (2)
        pixels.fill((g,r,b))
        pixels.show()
        return 'ok'
    else:
        return 'brightness not in [0, 1]', 400
