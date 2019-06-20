import pyxel
import constants 
import random

class Gachi:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_side = [-16, 16, 16, 16, 16, 16]
        self.y_side = [16, -16, 16, 16, 16, 16, 16, 16, 16, 16]
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 48, self.x_side[random.randint(0,len(self.x_side) - 1)], self.y_side[random.randint(0,len(self.y_side) - 1)], 0)