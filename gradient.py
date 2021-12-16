import board
import math
from time import sleep

import neopixel

R = 255
G = 180
B = 100
BRIGHTNESS = 0.15
NUM_PIXELS = 100
pixels = neopixel.NeoPixel(board.D21, NUM_PIXELS, auto_write=False)

steps = 200

def rgb_from_step(step, num_steps):
    rad = step / num_steps * 2 * math.pi
    r = math.floor(127.5 + 127.5 * math.sin(rad))
    g = math.floor(127.5 + 127.5 * math.sin(rad + 2 * math.pi / 3))
    b = math.floor(127.5 + 127.5 * math.sin(rad + 2 * 2 * math.pi / 3))
    return r, g, b

if __name__ == '__main__':
    while True:
        for step in range(steps):
            for i in range(NUM_PIXELS):
                r,g,b = rgb_from_step((step + i) % steps, steps)
                pixels[NUM_PIXELS - 1 - i] = (g, r, b)
            pixels.show()
    pixels.fill((G,R,B))
    pixels.show()
