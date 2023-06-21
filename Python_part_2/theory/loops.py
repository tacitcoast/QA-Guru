import random


# While - цикл с предусловием
# пока пользователь не введет правильный номер, ...

# while True:
#     print("Hello, world!")


required_number = 7
user_number = random.randint(0, 10)

while user_number != required_number:
    print(f"{user_number=} не равен {required_number}")
    user_number = random.randint(0, 10)
    print()


iterations_count = 10
i = 0

while i != iterations_count:
    print(i)
    i += 1

    # i = i + 1
    # i *= 1
    # i -= 1

# For. Итерируем списки и словари

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

for user in users:
    print(user)

d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for key in d:
    print(key)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

# for value in []:
#     print(123)

# Break/Continue/Else - прерывание цикла

# for i in range - цикл с итератором

print(list(range(10)))

print("-------------Начинаем цикл-----------")

for i in range(6):
    if i == 7:
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Когда я выполняюсь?")


print("------------------------")

for i in range(5, 25, 4):
    print(i)

print("------------------------")

for i in range(10, -10, -2):
    print(i)


# enumerate - возвращает пары (индекс, значение)


cities = ["Екатеринбург", "Москва", "Сочи"]

print("------------------------")

for city in cities:
    print(city)

for i, city in enumerate(cities):
    # print(city)
    print(f"{city} на {i + 1} месте по загрязнению воздуха")

for city in enumerate(cities):
    print(i)
