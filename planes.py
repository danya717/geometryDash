import arcade


class Plane(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.5)


    def update(self):
        self.center_y -= self.change_y


class OrangePlane(Plane):
    def __init__(self):
        super().__init__('bgs/orng_cube_plane.png')
        self.orange_plane = arcade.load_texture('bgs/orng_cube_plane.png')
        self.center_x = 300
        self.center_y = 171


