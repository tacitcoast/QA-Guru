
# Boolean - 3 состояния

b = bool

t = True
f = False
n = None


if t is True:
    pass
elif f is False:
    pass


if not True:
    print("Выражение истинно")
else:
    print("Выражение ложное")

# if/elif/else

code = 200

if code < 400:
    print("Хороший ответ")
    print()
    print()
elif 400 <= code < 500:
    print("Плохой запрос")
elif code >= 500:
    print("Серверу плохо")
else:
    print("Что-то неожиданное")


print(bool(123))
print(bool(-100))
print(bool(0))

print(bool("Hello, world!"))
print(bool(" "))
print(bool(""))

print(bool([1, 2, 3]))
print(bool([]))
print(bool([False]))

print(bool({}))

# Пустые объекты - false

user_list = []

if user_list:
    pass

items_count = 0

if not (n is None):
    pass


d = {"key": "value"}

n = d.get("another_key")

print(n)

if not (n is None):
    pass
