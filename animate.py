# import arcade
#
#
# class Animate(arcade.Sprite):
#     i = 0
#     time = 1
#
#     def update_animation(self, delta_time):
#         self.time += delta_time
#         if self.time >= 0.2:
#             self.time = -0.1
#             if self.i == len(self.textures) - 1:
#                 self.i = 0
#             else:
#                 self.i += 1
#             self.set_texture(self.i)