import os.path
import requests


def test_download_png():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open(os.path.abspath('../tmp/selenium_logo.png'), 'wb') as file:
        file.write(response.content)

    size = os.path.getsize('selenium_logo.png')

    assert 30803 == size
