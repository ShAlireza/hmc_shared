import requests
from typing import Union, Any, Tuple, Dict


def request(
        method: str,
        url: str,
        params: Dict[str, Union[str, int, float]] = None,
        json: Dict[str, Any] = None,
        headers: Dict[str, Union[str, int, float]] = None,
        cookies: Dict[str, Union[str, int, float]] = None,
) -> Tuple[Dict[str, Any], int]:
    params = {} if not params else params
    json = {} if not json else json

    response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            cookies=cookies
    )
    data = response.json()
    status_code = response.status_code

    return data, status_code
