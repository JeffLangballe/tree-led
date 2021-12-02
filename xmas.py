import neopixel
from time import sleep

r = 255
g = 180
b = 100

if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.D21, 100, brightness=0.15)
    pixels.fill((0,0,0))
    sleep (2)
    pixels.fill((g,r,b))
    pixels.show()
