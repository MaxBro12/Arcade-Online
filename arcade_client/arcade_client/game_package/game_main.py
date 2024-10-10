import arcade
from client_package import Client
from client_package.client_socket import ClientSocket
from core.debug import create_log
from core.settings_toml import load_settings, save_settings
from time import time


class Game(arcade.Window):
    def __init__(self):
        # ! Настройки
        self.settings = load_settings()

        # ! Server
        self.server = ClientSocket()
        create_log(f'status: {self.server.status.status} ping: {self.server.status.ping}')

        # ! Arcade
        super().__init__(
            width=self.settings.window.width,
            height=self.settings.window.height,
            title='Arcade Online',
            fullscreen=self.settings.window.fullscreen,
            resizable=self.settings.window.resizeable,
            vsync=self.settings.window.vsync,
            #update_rate=self.settings.window.max_fps # TODO: Что-то тут не то
        )

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        print(self.server.status)
        arcade.draw_text(
            f"Server: {self.server.status.status} Ping: {self.server.status.ping}",
            self.settings.window.width / 2,
            self.settings.window.height / 2,
            arcade.color.WHITE,
            30,
            anchor_x="right"
        )