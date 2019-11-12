import random

import arcade
from ap_game_constants import *
from ada_potato_sprite import AdaOrPotato

# Define constants

class AdaOrPotatoGame(arcade.Window):
    sprites: arcade.SpriteList[AdaOrPotato]
    score: int

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.score = None
        self.sprites = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.score = 0
        self.sprites = arcade.SpriteList()
        self.sprites.append(AdaOrPotato())
        self.sprites.append(AdaOrPotato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.sprites.draw()
        arcade.draw_text(str(self.score), 0, 0, arcade.color.WHITE, 50)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.sprites.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for sprite in self.sprites:
            if sprite.collides_with_point([x, y]):
                self.score += sprite.get_current_value()


def main():
    window = AdaOrPotatoGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
