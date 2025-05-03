import arcade


class Stinger(arcade.Sprite):
    def __init__(self):
        super().__init__('bgs/stinger-Photoroom.png', 1)
        self.center_x = 1370
        self.center_y = 157

    def update(self):
        self.center_x -= self.change_x

