import arcade
from .scenes import *
from typing import Union, Optional
import json


class Display(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Three of a king")
        self.title = arcade.sprite_list
        arcade.set_background_color((255, 255, 255))
        self.music_bool = True
        self.music = None
        with open("data/music.json") as file:
            self.music_load = json.load(file)
        self.scene = "loading"
        self.scenes = dict()
        self.processes = []
        self.music_play()

    def setup(self):
        self.scenes["loading"] = LoadingScreen(self)
        self.scenes["lobby"] = Lobby(self)
        self.scenes["mainMenu"] = MainMenu(self)
        self.scenes["options"] = Options(self)
        self.scenes["playClient"] = PlayAsClient(self)
        self.scenes["playServer"] = PlayAsServer(self)
        self.scenes["game"] = Game(self)
        self.scenes["victory"] = Victory(self)

    def change_scenes(self, scene: str, *args, **kwargs):
        self.scenes[scene].reset(*args, **kwargs)
        self.scene = scene
        if self.music_bool:
            self.music_play()

    def on_draw(self):
        arcade.start_render()
        self.scenes[self.scene].draw()
        if self.music.get_stream_position() == 0.0 and self.music_bool == True:
            self.music_play()

    def music_play(self):
        if self.scene in self.music_load:
            if self.music is not None:
                self.music.stop()
            self.music = arcade.Sound(self.music_load[self.scene], streaming=True)
            self.music.play(0.01)

    def on_update(self, delta_time: float):
        self.scenes[self.scene].update(delta_time)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.scenes[self.scene].mouse_release(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        self.scenes[self.scene].key_press(key, modifiers)

    def on_close(self):
        for process in self.processes:
            process.terminate()
        arcade.close_window()


def main():
    display1 = Display()
    display1.setup()
    arcade.run()
