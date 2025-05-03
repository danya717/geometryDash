import arcade

class Explosion(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.1)


class BasicCubeExp(Explosion):
    def __init__(self):
        super().__init__('bgs/basicCubeExpl-Photoroom.png')
        self.append_texture(arcade.load_texture('bgs/basicCubeExpl-Photoroom.png'))
        self.center_x = 157
        self.center_y = 169