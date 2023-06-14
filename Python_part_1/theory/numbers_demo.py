# Что там с числами? Присваиваем, считаем, используем разные системы счисления

# from decimal import Decimal

a = 100
a = 200
a = -300
a = 100 + 200
a = 300 - 100
a = 300 / 3
a = 100 * 100
a = 100 // 3
a = 3.5
a = (300 + 100) * 3
a = 5 ** 2
a = a * 10

print(a)


a = 0b1101001010
a = 0o1234567
a = 0x1234567abcdef

a = 984612461284790127471204701274091729047182497102739124107421
a = a - 1000000

print(a)

a = 0.1 + 0.2
# assert a == 0.3

print(a)


# Математика!

import math

math.pi


# Рандом!

import random

random.seed("another word")

print("RANDOM")

n = random.randint(0, 10)
print(n)
n = random.randint(0, 10)
print(n)
n = random.randint(0, 10)
print(n)

print("RANDOM")

print(round(1.333333, 2))
