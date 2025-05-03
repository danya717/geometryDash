import arcade


class Blocks(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.9)

    def update(self):
        self.center_x -= self.change_x


class BasicBlock(Blocks):
    def __init__(self):
        super().__init__('bgs/block-Photoroom.png')
        self.append_texture(arcade.load_texture('bgs/block-Photoroom.png'))
        self.center_x = 700
        self.center_y = 130
