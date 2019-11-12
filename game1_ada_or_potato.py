from typing import List, Optional

import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"

TIMER_MAXIMUM = 100

ADA_IMAGE = arcade.load_texture("images/ada.png")
POTATO_IMAGE = arcade.load_texture("images/potato.png")


class AdaOrPotato(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.texture = ADA_IMAGE
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
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


class AdaOrPotatoGame(arcade.Window):
    sprites: arcade.SpriteList[AdaOrPotato]
    score: int

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.score = 0
        self.sprites = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.score = 0
        self.sprites = arcade.SpriteList()
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
