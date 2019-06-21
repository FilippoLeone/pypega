import pyxel
import constants as c

class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = ''
        self.is_attacking = False
        self.hp = c.actor_hp

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
    
    def get_direction(self):
        return self.direction

    def is_attacking(self):
        return self.is_attacking

    def draw_hp_bar(self):
        pyxel.text(17, 10, self.get_hp(), 8)
        pyxel.blt(2, 10, 0, 48, 48, 16, 16, 0)
        pyxel.blt(18, 10, 0, 48+16, 48, 16, 16, 0)
        pyxel.blt(34, 10, 0, 48+32, 48, 16, 16, 0)
        pyxel.blt(50, 10, 0, 48+48, 48, 16, 16, 0)

    def get_hp(self):
        return (f"{self.hp}")

    def attack(self, direction):
        if direction == 'right':
            pyxel.blt(self.x+15, self.y, 0, 64, 32, 16, 16, 0)
        else:
            pyxel.blt(self.x-15, self.y, 0, 64, 32, -16, 16, 0)

    def shield(self, direction):
        if direction == 'right':
            pyxel.blt(self.x+12, self.y, 0, 80, 32, 16, 16, 0)
        else:
            pyxel.blt(self.x-12, self.y, 0, 80, 32, -16, 16, 0)   

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




