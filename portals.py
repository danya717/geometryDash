import arcade


class Portals(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.9)


class FlyPortal(Portals):
    def __init__(self):
        super().__init__('bgs/fly_portal_adb.png')
        self.fly_portal = arcade.load_texture('bgs/fly_portal_adb.png')
        self.center_x = 500
        self.center_y = 130

    def update(self):
        self.center_x -= self.change_x