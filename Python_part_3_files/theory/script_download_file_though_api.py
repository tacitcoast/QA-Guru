import os

import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'

response = requests.get(url)

with open('selenium_logo_square_green.png', 'wb') as file:
    file.write(response.content)

with open('selenium_logo_square_green.png', 'rb') as file:
    selenium_png = file.read()
    print(len(selenium_png))


print(os.path.getsize('selenium_logo_square_green.png'))
