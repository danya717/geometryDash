import arcade
import animate
from conststants import *


class Cubes(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.7)
        self.angle = 0

    def update(self):
        self.center_y += self.change_y
        self.change_y -= 1
        if self.center_y < 175:
            self.change_y = 175
            self.change_y = 0
        self.angle -= self.change_angle
        if self.angle <= -LIMIT_ANGLE:
            self.angle = -LIMIT_ANGLE


class BasicOrangeCube(Cubes):
    def __init__(self):
        super().__init__('cubes/b_orange_c.png')
        self.append_texture(arcade.load_texture('cubes/b_orange_c.png'))
        self.center_x = 156
        self.center_y = 171


class BasicBlueCube(Cubes):
    def __init__(self):
        super().__init__('cubes/b_blue_c.png')
        self.append_texture(arcade.load_texture('cubes/b_blue_c.png'))
        self.center_x = 156
        self.center_y = 171


class BasicYellowCube(Cubes):
    def __init__(self):
        super().__init__('cubes/b_yellow_c.png')
        self.append_texture(arcade.load_texture('cubes/b_yellow_c.png'))
        self.center_x = 156
        self.center_y = 171


class BasicRedCube(Cubes):
    def __init__(self):
        super().__init__('cubes/b_red_c.png')
        self.append_texture(arcade.load_texture('cubes/b_red_c.png'))
        self.center_x = 156
        self.center_y = 171