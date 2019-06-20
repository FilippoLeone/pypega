import pyxel
import constants as c

class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = ''
    
    def __del__(self):
        pass

    def move(self, x, y):
        if x > 0 and y == 0:
            self.x = self.x + x
            self.direction = 'Right'
        if x < 0 and y == 0:
            self.x = self.x + x
            self.direction = 'Left'
        if y > 0 and x == 0 or y < 0 and x == 0:
            self.y = self.y + y
        
    def get_position(self):
        return self.x, self.y
    
    def draw(self):
        if self.is_jumping() and self.direction == 'Left':
            pyxel.blt(self.x, self.y, 0, 0, 48, -16, -16, 0)
        elif self.is_jumping():
            pyxel.blt(self.x, self.y, 0, 0, 48, 16, -16, 0)
        elif self.direction == 'Right':
            pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)
        elif self.direction == 'Left':
            pyxel.blt(self.x, self.y, 0, 0, 48, -16, 16, 0)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)

    def draw_hands(self):
        if self.is_jumping() and self.direction == 'Left':
            pyxel.blt(self.x, self.y, 0, 16, 64, -16, -16, 0)
            pyxel.blt(self.x-15, self.y, 0, 0, 64, -16, -16, 0)
            pyxel.blt(self.x+15, self.y, 0, 32, 64, -16, -16, 0)
        elif self.is_jumping():
            pyxel.blt(self.x, self.y, 0, 16, 64, 16, -16, 0)
            pyxel.blt(self.x-15, self.y, 0, 0, 64, 16, -16, 0)
            pyxel.blt(self.x+15, self.y, 0, 32, 64, 16, -16, 0)
        elif self.direction == 'Right':
            pyxel.blt(self.x, self.y, 0, 16, 64, 16, 16, 0)
            pyxel.blt(self.x-10, self.y, 0, 0, 64, 16, 16, 0)
            pyxel.blt(self.x+12, self.y, 0, 32, 64, 16, 16, 0)
        elif self.direction == 'Left':
            pyxel.blt(self.x-15, self.y, 0, 0, 64, -16, 16, 0)
            pyxel.blt(self.x+15, self.y, 0, 32, 64, -16, 16, 0)
            pyxel.blt(self.x, self.y, 0, 16, 64, -16, 16, 0)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 64, 16, 16, 0)
            pyxel.blt(self.x-10, self.y, 0, 32, 64, 16, 16, 0)
            pyxel.blt(self.x+12, self.y, 0, 16, 64, 16, 16, 0)

    def is_in_limit(self):
        if self.y < c.baseline:
            return True
        return False

    def is_jumping(self):
        try:
            if int(self.y) < int(self.previous_y) and self.y < c.baseline - 2:
                return True
        except AttributeError:
            pass
        self.previous_y = self.y 
        return False

    def applygravity(self, intensity):
        self.y = self.y + intensity

    def jump(self, intensity, startpoint):
        self.startpoint = startpoint
        self.y = self.y - intensity




