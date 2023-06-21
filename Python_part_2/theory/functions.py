

# Объявляем функцию

def my_function():
    print("Hello, world!")


my_function()


# Функция с позиционными аргументами

def my_custom_print(line):
    print(line)


my_custom_print("Hello, world!")
my_custom_print("Hello again!")


# Функция с именованными аргументами

def my_another_print(line, separator=" "):
    print(line, sep=separator)


my_another_print(line="Hello, world!", separator="----")
my_another_print(separator="----", line="Hello!")


# Функция с аргументами по умолчанию

my_another_print(line="Hello!")

# Поговорить про None


def custom_print(line, wrapped_symbol=None):
    if wrapped_symbol is None:
        print(line)
    else:
        print(f"{wrapped_symbol}{line}{wrapped_symbol}")


custom_print("Hello, world!")
custom_print("Hello, world!", wrapped_symbol="***")

# Возвращаем значение


def sum_numbers(a, b):
    return a + b


assert sum_numbers(5, 10) == 15


# Возвращаем несколько значений

def return_many_numbers():
    return 5, 10, 15


result = return_many_numbers()

a, b, c = return_many_numbers()

print(a)

a, _, _ = return_many_numbers()
*_, b, _ = return_many_numbers()

print(a, b, c)

a, *_ = return_many_numbers()

*_, c = return_many_numbers()

print()

# Переменное количество аргументов на примере print


def awesome_print(*lines):
    # for line in lines:
    #     print(line)
    print(lines)
    print(*lines)
    print(*lines, sep=" | ")


awesome_print("Hello", ", ", "world!", "Эта строка будет четвертым аргументом")

# Переменное кол-во именованных аргументов


def named_print(**kwargs):
    for item in kwargs.items():
        print(item)


named_print(first="Hello", second="World")

# Область видимости переменных

print("-------------")
n = 10


def func():
    import math

    print(n)

func()

print(n)


# Функция - тоже объект

p = print

p("Hello, world!")

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]


def get_age(user):
    print("Я вызвана для", user)
    return user["age"]



from operator import itemgetter


# users.sort(key=get_age)

# users.sort(key=lambda user: user["age"])

users.sort(key=itemgetter("age"))


from pprint import pprint
pprint(users)
