import pyxel
import constants as c
import random

class Gachi:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_side = [-16, 16, 16, 16, 16, 16]
        self.y_side = [16, -16, 16, 16, 16, 16, 16, 16, 16, 16]
        self.hp = c.gachi_hp

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 48, self.x_side[random.randint(0,len(self.x_side) - 1)]
        , self.y_side[random.randint(0,len(self.y_side) - 1)]
        , 0)
        
    def draw_hp_bar(self):
        pyxel.text(17, 10, self.get_hp(), 8)
        pyxel.blt(-2, 10, 0, 48, 48, 16, 16, 0)
        pyxel.blt(-18, 10, 0, 48+16, 48, 16, 16, 0)
        pyxel.blt(-34, 10, 0, 48+32, 48, 16, 16, 0)
        pyxel.blt(-50, 10, 0, 48+48, 48, 16, 16, 0)

    def get_hp(self):
        return (f"{self.hp}")