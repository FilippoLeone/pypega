import pyxel
import constants as c

class Levels:
    def __init__(self):
        self.virtual_x = 0
        self.virtual_y = 0

    def draw(self):
        pyxel.bltm(self.virtual_x, self.virtual_y, 0, 0, 0, 256, 16, 0)

    def move(self, direction, x):

        if direction == 'right':
            self.virtual_x = -x
            pyxel.bltm(self.virtual_x, self.virtual_y, 0, 0, 0, 256, 16, 0)
            #print(f"blitting tilemap at: {self.virtual_x}")

        if direction == 'left':
            self.virtual_x = -x
            pyxel.bltm(self.virtual_x, self.virtual_y, 0, 0, 0, 256, 16, 0)
            #print(f"blitting tilemap at: {self.virtual_x}")