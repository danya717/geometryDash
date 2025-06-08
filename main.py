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
from blocks import BasicBlock2
from blocks import BlockBarrier
from portals import FlyPortal
from planes import OrangePlane


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('bgs/mainBg.png')
        self.lobby_bg = arcade.load_texture('bgs/gmdMenu2.png')
        self.creating = arcade.load_texture('bgs/creator.png')
        self.loading = arcade.load_texture('bgs/loading.png')
        # self.orange_plane = arcade.load_texture('bgs/orng_cube_plane.png')
        self.basic_orange_cube = BasicOrangeCube()
        self.basic_blue_cube = BasicBlueCube()
        self.basic_red_cube = BasicRedCube()
        self.basic_yellow_cube = BasicYellowCube()
        self.stinger = Stinger()
        self.stinger2 = Stinger2()
        self.basic_block = BasicBlock()
        self.basic_block2 = BasicBlock2()
        self.block_barrier = BlockBarrier()
        self.fly_portal = FlyPortal()
        self.orange_plane = OrangePlane()
        self.cube_apper_time = time.time()
        self.next_bg_time = time.time()
        self.line_reducer_time = time.time()
        self.death_sound = arcade.load_sound('sounds/geometry-dash-death-sound-effect.mp3')
        self.menu_sound = arcade.load_sound('sounds/gmd_menu_sound.mp3')
        self.click_sound = arcade.load_sound('sounds/gmdClickSound.mp3')
        self.line_reducer = 40
        self.lvl_line_reducer = 70
        self.game = False
        self.active = False
        self.load = False
        self.create_bg = False
        self.jump = False
        self.attempts = 0
        self.plane_show = False
        self.cube_show = False

    def setup(self):
        pass

    def on_draw(self):
        if self.game:
            self.clear()
            indent = 10 * self.lvl_line_reducer
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            arcade.draw_text(f'Attempt: {int(self.attempts)}', 500, 650, (255, 255, 255),
                             65)
            arcade.draw_rectangle_filled(700 - indent / 2, 785, 700 - indent, 15, (55, 55, 55))
            arcade.draw_rectangle_outline(700, 785, 700, 15, (255, 255, 255), 1)
            if self.cube_show:
                self.basic_orange_cube.draw()
                self.plane_show = False
            if self.plane_show:
                self.orange_plane.draw()
                self.cube_show = False
            self.stinger.draw()
            self.basic_block.draw()
            self.stinger2.draw()
            self.basic_block2.draw()
            self.block_barrier.draw()
            self.fly_portal.draw()
            self.cube_show = True
            self.plane_show = False
            #     arcade.draw_scaled_texture_rectangle(100, 100, self.orange_plane)
        if not self.game:
            self.load = True
            indent = 12.5 * self.line_reducer
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.loading)
            arcade.draw_rectangle_filled(690 - indent / 2, 266, 500 - indent, 15, (0, 255, 255))
            arcade.draw_rectangle_outline(690, 266, 500, 15, (255, 255, 0), 2)
            if time.time() - self.next_bg_time > 5.5:
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
            self.basic_block2.update()
            self.basic_block2.change_x = STINGER_MOVE
            self.block_barrier.update()
            self.block_barrier.change_x = STINGER_MOVE
            self.fly_portal.update()
            self.fly_portal.change_x = STINGER_MOVE
            if self.plane_show:
                self.orange_plane.update()
                self.orange_plane.change_x = STINGER_MOVE
        if self.stinger.center_x < SCREEN_WIDTH - 1500:
            self.stinger.center_x = 1370
        if self.stinger2.center_x < SCREEN_WIDTH - 1500:
            self.stinger2.center_x = self.stinger.center_x + 200
        if self.basic_block.center_x < SCREEN_WIDTH - 1500:
            self.basic_block.center_x = 1800
        if self.basic_block2.center_x < SCREEN_WIDTH - 1500:
            self.basic_block2.center_x = self.basic_block.center_x + 50
        if not self.cube_show:
            if arcade.check_for_collision(self.stinger, self.basic_orange_cube):
                self.basic_orange_cube.alpha = 0
                self.cube_apper_time = time.time()
                self.stinger.center_x = 1370
                self.stinger2.center_x = self.stinger.center_x + 200
                self.basic_block.center_x = 1800
                self.basic_block2.center_x = 1850
                self.block_barrier.center_x = 1795
                self.attempts += 1
                self.lvl_line_reducer = 70
                arcade.play_sound(self.death_sound, 1)
        if arcade.check_for_collision(self.stinger2, self.basic_orange_cube):
            self.basic_orange_cube.alpha = 0
            self.cube_apper_time = time.time()
            self.stinger.center_x = 1370
            self.stinger2.center_x = self.stinger.center_x + 200
            self.basic_block.center_x = 1800
            self.basic_block2.center_x = 1850
            self.block_barrier.center_x = 1795
            self.attempts += 1
            self.lvl_line_reducer = 70
            arcade.play_sound(self.death_sound, 1)
        if self.basic_orange_cube.alpha == 0 and time.time() - self.cube_apper_time > 0.01:
            time.sleep(1.5)
            self.basic_orange_cube.alpha = 255
        # if arcade.check_for_collision(self.basic_orange_cube, self.basic_block):
        #     self.basic_orange_cube.center_y = self.basic_block.center_y + 100
        # if arcade.check_for_collision(self.basic_orange_cube, self.basic_block2):
        #     self.basic_orange_cube.center_y = self.basic_block2.center_y + 100
        if arcade.check_for_collision(self.basic_orange_cube, self.block_barrier):
            self.basic_orange_cube.alpha = 0
            self.cube_apper_time = time.time()
            self.stinger.center_x = 1370
            self.basic_block.center_x = 1800
            self.basic_block2.center_x = 1850
            self.block_barrier.center_x = 1745
            self.attempts += 1
        if arcade.check_for_collision(self.basic_orange_cube, self.basic_block):
            self.basic_orange_cube.center_y = self.basic_block.center_y + 100
        # if arcade.check_for_collision(self.basic_orange_cube, self.fly_portal):
        if self.basic_orange_cube.right > self.fly_portal.left:
            if self.game:
                self.plane_show = True
                self.cube_show = False

        if self.basic_orange_cube.alpha == 0 and time.time() - self.cube_apper_time > 0.01:
            time.sleep(1.5)
            self.basic_orange_cube.alpha = 255
        # if not self.game:
        # arcade.play_sound(self.menu_sound, 0.5)
        if not self.game:
            if time.time() - self.line_reducer_time > 1:
                self.line_reducer = 38
                if time.time() - self.line_reducer_time > 2:
                    self.line_reducer = 28
                    if time.time() - self.line_reducer_time > 3:
                        self.line_reducer = 15
                        if time.time() - self.line_reducer_time > 4:
                            self.line_reducer = 9
                            if time.time() - self.line_reducer_time > 5:
                                self.line_reducer = 0
        if self.game:
            if self.lvl_line_reducer > 0:
                if time.time() - self.line_reducer_time > 1:
                    self.lvl_line_reducer -= 0.08

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
                print(self.creating.name)
                self.creating = self.lobby_bg
                print(self.creating.name)

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
