from server_package import Server
from core.debug import create_log


class Game:
    def __init__(self):

        # ! Server
        self.server = Server()
        st = self.server.status()
        create_log(f'status: {st.status} ping: {st.ping}')