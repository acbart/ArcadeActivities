import arcade
import random
from ap_game_constants import *

ADA_IMAGE = arcade.load_texture("images/ada.png", scale=.25)
POTATO_IMAGE = arcade.load_texture("images/potato.png", scale=.25)


class AdaOrPotato(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.texture = ADA_IMAGE
        self.timer = 0
        self.center_x = random.randint(0, WINDOW_WIDTH)
        self.center_y = WINDOW_HEIGHT / 2

    def update(self):
        self.timer += 1
        if self.timer > TIMER_MAXIMUM:
            self.timer = 0
            self.switch_image()

    def switch_image(self):
        if self.texture == ADA_IMAGE:
            self.texture = POTATO_IMAGE
        else:
            self.texture = ADA_IMAGE

    def get_current_value(self):
        if self.texture == ADA_IMAGE:
            return 1
        else:
            return -1