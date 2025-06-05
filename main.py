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
from stinger import Stinger2


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = False
        self.bg = arcade.load_texture('bgs/mainBg.png')
        self.basic_orange_cube = BasicOrangeCube()
        self.basic_blue_cube = BasicBlueCube()
        self.basic_red_cube = BasicRedCube()
        self.basic_yellow_cube = BasicYellowCube()
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
        self.create_bg = False
        self.stinger2 = Stinger2()

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
            self.stinger2.draw()
        if not self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.lobby_bg)

        if self.create_bg:
            arcade.draw_text('Your cube is:', 507, 718, (0, 0, 0), 50)
            arcade.draw_text('X', 34, 755, (0, 0, 0), 20)
            self.basic_blue_cube.draw()
            self.basic_yellow_cube.draw()
            self.basic_red_cube.draw()

    def update(self, delta_time):
        self.basic_orange_cube.update()
        if self.game:
            self.stinger.update()
            self.stinger.change_x = STINGER_MOVE
            self.stinger2.update()
            self.stinger2.change_x = STINGER_MOVE
            self.basic_block.update()
            self.basic_block.change_x = STINGER_MOVE
        if self.stinger.center_x < SCREEN_WIDTH - 1500:
            self.stinger.center_x = 1370
        if self.stinger2.center_x < SCREEN_WIDTH - 1500:
            self.stinger2.center_x = self.stinger.center_x + 200
        if arcade.check_for_collision(self.stinger, self.basic_orange_cube):
            self.basic_orange_cube.alpha = 0
            self.cube_apper_time = time.time()
            self.stinger.center_x = 1370
            self.stinger2.center_x = self.stinger.center_x + 200
            self.basic_block.center_x = 800
            self.attempts += 1
            arcade.play_sound(self.death_sound, 1)
        if arcade.check_for_collision(self.stinger2, self.basic_orange_cube):
            self.basic_orange_cube.alpha = 0
            self.cube_apper_time = time.time()
            self.stinger.center_x = 1370
            self.stinger2.center_x = self.stinger.center_x + 200
            self.basic_block.center_x = 800
            self.attempts += 1
            arcade.play_sound(self.death_sound, 1)
        if self.basic_orange_cube.alpha == 0 and time.time() - self.cube_apper_time > 0.01:
            time.sleep(1.5)
            self.basic_orange_cube.alpha = 255
            self.basic_cube_exp.draw()
        # if self.basic_orange_cube.right > self.basic_block. eft:
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
                    self.basic_orange_cube.change_angle = 3.5
        if key == arcade.key.E:
            self.game = True

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:
            if ZONE_X_7 <= x <= ZONE_X_7 + ZONE_WIDTH_7 and ZONE_Y_7 <= y <= ZONE_Y_7 + ZONE_HEIGHT_7:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    if self.basic_orange_cube.center_y <= GROUND_Y:
                        self.basic_orange_cube.angle = 0
                        self.basic_orange_cube.change_y = CUBE_JUMP
                        self.basic_orange_cube.change_angle = 3.5
        if not self.game:
            if ZONE_X_1 <= x <= ZONE_X_1 + ZONE_WIDTH_1 and ZONE_Y_1 <= y <= ZONE_Y_1 + ZONE_HEIGHT_1:
                print('aa')
                arcade.play_sound(self.click_sound, 0.5)
                self.game = True
            print(x, y)
            if ZONE_X_2 <= x <= ZONE_X_2 + ZONE_WIDTH_2 and ZONE_Y_2 <= y <= ZONE_Y_2 + ZONE_HEIGHT_2:
                self.create_bg = True
                arcade.play_sound(self.click_sound, 0.5)
                self.lobby_bg = self.creating
            if ZONE_X_3 <= x <= ZONE_X_3 + ZONE_WIDTH_3 and ZONE_Y_3 <= y <= ZONE_Y_3 + ZONE_HEIGHT_3:
                self.basic_blue_cube.center_x = 695
                self.basic_blue_cube.center_y = 627
                self.basic_yellow_cube.center_x = 405
                self.basic_yellow_cube.center_y = 370
                self.basic_red_cube.center_x = 476
                self.basic_red_cube.center_y = 370
            if ZONE_X_4 <= x <= ZONE_X_4 + ZONE_WIDTH_4 and ZONE_Y_4 <= y <= ZONE_Y_4 + ZONE_HEIGHT_4:
                self.create_bg = False
                self.creating = self.lobby_bg
            if ZONE_X_5 <= x <= ZONE_X_5 + ZONE_WIDTH_5 and ZONE_Y_5 <= y <= ZONE_Y_5 + ZONE_HEIGHT_5:
                print('hi')
                self.basic_blue_cube.center_x = 334
                self.basic_blue_cube.center_y = 370
                self.basic_yellow_cube.center_x = 695
                self.basic_yellow_cube.center_y = 627
                self.basic_red_cube.center_x = 476
                self.basic_red_cube.center_y = 370
            if ZONE_X_6 <= x <= ZONE_X_6 + ZONE_WIDTH_6 and ZONE_Y_6 <= y <= ZONE_Y_6 + ZONE_HEIGHT_6:
                print('hi')
                self.basic_blue_cube.center_x = 334
                self.basic_blue_cube.center_y = 370
                self.basic_yellow_cube.center_x = 405
                self.basic_yellow_cube.center_y = 370
                self.basic_red_cube.center_x = 695
                self.basic_red_cube.center_y = 627


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
