
import arcade
import pyglet
import pyglet.gl as gl

import Level
import Keyboard
import Camera

WIDTH = 300
HEIGHT = 200
TITLE = "Python Game Jam 2020"

class PyGameJam2020(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        self.frames = 0
        self.time = 0

        self.mouse_x = 0
        self.mouse_y = 0

        self.zoom_width = WIDTH
        self.zoom_height = HEIGHT

        self.camera = Camera.Camera(WIDTH, HEIGHT)
        self.keyboard = Keyboard.Keyboard()

        self.set_location((self.camera.screen_width - WIDTH) // 2, (self.camera.screen_height - HEIGHT) // 2)

    def setup(self):
        self.level = Level.Level(self.camera, self.keyboard)

    def on_update(self, delta):

        self.level.update(delta)

        self.camera.x = self.level.player.center_x
        self.camera.y = self.level.player.center_y

        self.frames += 1
        self.time += delta

        if self.time >= 1:
            print(f"FPS: {self.frames} | Time: {self.time}")
            self.time -= 1
            self.frames = 0

    def on_draw(self):
        arcade.start_render()

        self.camera.set_viewport()

        self.level.draw()

    def on_key_press(self, key, modifiers):
        self.keyboard.on_key_press(key, modifiers)

        if key == arcade.key.EQUAL:
            self.camera.zoom(0.9)
        elif key == arcade.key.MINUS:
            self.camera.zoom(1/0.9)
    
    def on_key_release(self, key, modifiers):
        self.keyboard.on_key_release(key, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

def main():
    window = PyGameJam2020()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()