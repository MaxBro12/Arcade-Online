import requests
from core.debug import create_log
from .client_dataclass import ResponseData


class ServerSession:
    session: requests.Session = requests.Session()

    def get(
            self,
            url: str,
            params: dict | None = None,
            headers: dict | None = None,
    ) -> ResponseData | None:
        try:
            res = self.session.get(
                url=url,
                params=params,
                headers=headers
            )
            return ResponseData(
                res.status_code,
                res.json()
            )
        except requests.exceptions.ConnectionError:
            create_log(f'Connection error {url}', 'error')
            return None

    def post(
            self,
            url: str,
            params: dict | None = None,
            headers: dict | None = None,
    ) -> ResponseData | None:
        try:
            res = self.session.post(
                url=url,
                params=params,
                headers=headers
            )
            return ResponseData(
                res.status_code,
                res.json()
            )
        except requests.exceptions.ConnectionError:
            create_log(f'Connection error {url}', 'error')
            return None

    def update_session(self):
        self.session = requests.Session()
