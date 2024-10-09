import arcade
from server_package import Server
from core.debug import create_log
from core.settings_toml import load_settings, save_settings


class Game(arcade.Window):
    def __init__(self):
        # ! Настройки
        self.settings = load_settings()

        # ! Server
        self.server = Server()
        st = self.server.status()
        create_log(f'status: {st.status} ping: {st.ping}')

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