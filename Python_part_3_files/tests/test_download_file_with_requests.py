import os.path
import requests
from .conftest import path_tmp


def test_download_png():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open(os.path.join(path_tmp, 'selenium_logo.png'), 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(os.path.join(path_tmp, 'selenium_logo.png'))

    assert 30803 == size
