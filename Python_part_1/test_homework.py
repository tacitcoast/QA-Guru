from math import pi
import random


def test_greeting():
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    output_2 = "Привет, {}! Тебе {} лет.".format(name, age)

    assert output == "Привет, Анна! Тебе 25 лет."
    assert output_2 == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    perimeter = 2 * (a + b)
    assert perimeter == 60

    area = a * b
    assert area == 200


def test_circle():
    r = 23

    area = pi * r ** 2
    assert area == 1661.9025137490005

    length = 2 * pi * r
    assert length == 144.51326206513048


def test_random_list():
    l = []

    for i in range(10):
        l.append(random.randint(1, 100))
    l.sort()

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
