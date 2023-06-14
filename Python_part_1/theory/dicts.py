# Заводим словарики

d = {
    "key": 123,
    "second_key": 321
}

maria = {
    "name": "Maria",
    "age": "18",
    "hobbies": []
}

oleg = {
    "name": "Oleg",
    "age": "21",
    "hobbies": []
}

print(maria["age"])
print(oleg["age"])

maria["hobbies"].append("painting")

users = [maria, oleg]

# Функции словарей

print(list(maria.items()))
print(list(maria.keys()))
print(list(maria.values()))

# print(maria["unexpected"])
print(maria.get("name", "Это поле было пустым"))
print(maria.get("unexpected", "Это поле было пустым"))
