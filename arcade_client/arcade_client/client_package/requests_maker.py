import requests
from core.debug import create_log
from .client_dataclass import ResponseData


def make_get_request(
    url: str,
    params: dict | None = None,
    headers: dict | None = None,
) -> ResponseData | None:
    try:
        res = requests.get(
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