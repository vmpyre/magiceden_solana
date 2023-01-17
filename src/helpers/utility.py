import requests

def _make_request(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Error: {response.status_code}: {response.content}')
