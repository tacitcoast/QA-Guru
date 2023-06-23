import os

os.path.getsize('selenium_logo_square_green.png') # выдает размер файла

p = os.path.abspath(__file__)
print(p)

d = os.path.dirname(os.path.abspath(__file__))
print(d)

j = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
print(j)

