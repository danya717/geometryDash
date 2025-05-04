import arcade
from conststants import *
from stinger import Stinger
import time
from CubesExps import BasicCubeExp
from blocks import BasicBlock
from cubes import BasicBlueCube
from cubes import BasicRedCube
from cubes import BasicYellowCube
from cubes import BasicOrangeCube

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = False
        self.bg = arcade.load_texture('bgs/mainBg.png')
        self.basic_orange_cube = BasicOrangeCube()
        self.stinger = Stinger()
        self.jump = False
        self.lobby_bg = arcade.load_texture('bgs/gmdMenu2.png')
        self.attempts = 0
        self.cube_apper_time = time.time()
        self.basic_cube_exp = BasicCubeExp()
        self.basic_block = BasicBlock()
        self.creating = arcade.load_texture('bgs/creator.png')
        self.death_sound = arcade.load_sound('sounds/geometry-dash-death-sound-effect.mp3')
        self.menu_sound = arcade.load_sound('sounds/gmd_menu_sound.mp3')
        self.click_sound = arcade.load_sound('sounds/gmdClickSound.mp3')

    def setup(self):
        pass

    def on_draw(self):
        if self.game:
            self.clear()
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            arcade.draw_text(f'Attempt: {int(self.attempts)}', SCREEN_WIDTH - 850, SCREEN_HEIGHT - 100, (255, 255, 255),
                             65)
            self.basic_orange_cube.draw()
            self.stinger.draw()
            self.basic_block.draw()
        if not self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.lobby_bg)

            # arcade.draw_rectangle_filled(
            #     ZONE_X_2 + ZONE_WIDTH_2 / 2,
            #     ZONE_Y_2 + ZONE_HEIGHT_2 / 2,
            #     ZONE_WIDTH_2,
            #     ZONE_HEIGHT_2,
            #     arcade.color.LIGHT_BLUE)
            #
            # arcade.draw_rectangle_filled(
            #     ZONE_X_1 + ZONE_WIDTH_1 / 2,
            #     ZONE_Y_1 + ZONE_HEIGHT_1 / 2,
            #     ZONE_WIDTH_1,
            #     ZONE_HEIGHT_1,
            #     arcade.color.LIGHT_YELLOW)

    def update(self, delta_time):
        self.basic_orange_cube.update()
        if self.game:
            self.stinger.update()
            self.stinger.change_x = STINGER_MOVE
            self.basic_block.update()
            self.basic_block.change_x = STINGER_MOVE
        if self.stinger.center_x < SCREEN_WIDTH - 1500:
            self.stinger.center_x = 1370
        if arcade.check_for_collision(self.stinger, self.basic_orange_cube):
            self.basic_orange_cube.alpha = 0
            self.cube_apper_time = time.time()
            self.stinger.center_x = 1370
            self.basic_block.center_x = 800
            self.attempts += 1
            arcade.play_sound(self.death_sound, 1)
        if self.basic_orange_cube.alpha == 0 and time.time() - self.cube_apper_time > 0.01:
            time.sleep(1.5)
            self.basic_orange_cube.alpha = 255
            self.basic_cube_exp.draw()
        # if self.basic_orange_cube.right > self.basic_block.left:
        #     self.basic_orange_cube.alpha = 0
        #     self.cube_apper_time = time.time()
        #     self.stinger.center_x = 1370
        #     self.basic_block.center_x = 800
        #     self.attempts += 1
        if self.basic_orange_cube.alpha == 0 and time.time() - self.cube_apper_time > 0.01:
            time.sleep(1.5)
            self.basic_orange_cube.alpha = 255
        # if not self.game:
            # arcade.play_sound(self.menu_sound, 0.5)



    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.SPACE:
                if self.basic_orange_cube.center_y <= GROUND_Y:
                    self.basic_orange_cube.angle = 0
                    self.basic_orange_cube.change_y = CUBE_JUMP
                    self.basic_orange_cube.change_angle = 8.5
        if key == arcade.key.E:
            self.game = True

    def on_mouse_press(self, x, y, button, modifiers):
        if ZONE_X_2 <= x <= ZONE_X_2 + ZONE_WIDTH_2 and ZONE_Y_2 <= y <= ZONE_Y_2 + ZONE_HEIGHT_2:
            print('aa')
            arcade.play_sound(self.click_sound, 0.5)
            self.game = True
        print(x, y)
        if ZONE_X_1 <= x <= ZONE_X_1 + ZONE_WIDTH_1 and ZONE_Y_1 <= y <= ZONE_Y_1 + ZONE_HEIGHT_1:
            arcade.play_sound(self.click_sound, 0.5)
            self.lobby_bg = self.creating



window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
