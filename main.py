from playsound import playsound as player
import os
import pyxel
import constants as c
from game.characters.actor import Actor
from game.levels.level import Levels as lvl
from game.characters.enemy import Gachi

class App:
    def __init__(self):
        pyxel.init(c.resolution['x'], c.resolution['y'], caption=c.title)
        pyxel.load('game/assets/pypega.pyxres')
        self.x = 0;self.y = 0;self.virtual_x = 0
        self.level = lvl()
        self.actor = Actor(2, c.baseline) 
        self.gachi = Gachi(110, c.baseline - 55)
        self.gachi_on = False
        pyxel.run(self.update, self.draw)

        
    def update(self):
        if True:
            print(f"Current Position: {self.actor.get_position()}")
            #print(f"Jumping: {self.actor.is_jumping()}")
            print(f"Virtual X: {self.virtual_x}")
        self.x, self.y = self.actor.get_position()
        

        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_DOWN) and self.y < c.resolution['y'] - 40:
            self.actor.move(0, c.actor_speed)

        if pyxel.btnp(pyxel.KEY_SPACE) and self.y > 2 and self.actor.is_jumping() == False:
            self.actor.jump(c.actor_jump, self.y)

        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 2:
                self.actor.move(-c.actor_speed, 0)
            if self.virtual_x > 0:
                self.virtual_x = self.virtual_x - c.actor_speed

        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x < c.resolution['x'] - 28:
                self.actor.move(c.actor_speed, 0)
            if self.virtual_x < 1920:
                self.virtual_x = self.virtual_x + c.actor_speed


        if self.actor.is_in_limit():
            self.actor.applygravity(c.gravity['downforce'])


    def draw(self):
        pyxel.cls(0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.level.move('right', self.virtual_x)
        elif pyxel.btn(pyxel.KEY_LEFT) and self.virtual_x > 0:
            self.level.move('left', self.virtual_x)
        else:
            self.level.draw()

        #if self.gachi_on:
            #self.actor.draw_hands()
       # else:
        self.actor.draw()

        self.actor.draw_hp_bar()

        self.draw_attack()
        self.draw_shield()
        if self.virtual_x > 150 and self.virtual_x < 550 or self.gachi_on:
            self.gachi.draw()
            if not self.gachi_on:
                self.gachi_on = True
                player(os.getcwd()+r'\game\assets\music\assclap.mp3', False)

    def draw_attack(self):
        if pyxel.btn(pyxel.KEY_F) or pyxel.btn(pyxel.KEY_F) and pyxel.btn(pyxel.KEY_SPACE):
            if self.actor.get_direction() == 'Right':
                self.actor.attack('right')
            else:
                self.actor.attack('left')
        else:
            pass

    def draw_shield(self):
        if pyxel.btn(pyxel.KEY_E) or pyxel.btn(pyxel.KEY_E) and pyxel.btn(pyxel.KEY_SPACE):
            if self.actor.get_direction() == 'Right':
                self.actor.shield('right')
            else:
                self.actor.shield('left')
        else:
            pass

if __name__ == '__main__':
    App()