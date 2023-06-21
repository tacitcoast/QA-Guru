from datetime import time


# Тестирование переключения темной темы на сайте в зависимости от времени
def test_dark_theme_by_time():
    current_time = time(hour=23)
    is_dark_theme = 6 < current_time.hour >= 22

    assert is_dark_theme is True


# Тестирование переключения темной темы на сайте в зависимости от времени и выбора пользователя
def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = None

    if dark_theme_enabled_by_user is None:
        if 6 < current_time.hour >= 22:
            is_dark_theme = True
    else:
        is_dark_theme = dark_theme_enabled_by_user

    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Ищем пользователя с именем "Olga"
    suitable_users = None

    for i in users:
        if i["name"] == "Olga":
            suitable_users = i

    assert suitable_users == {"name": "Olga", "age": 45}

    # Ищем всех пользователей младше 20 лет
    suitable_users = None
    suitable_users = []

    for i in users:
        if i["age"] < 20:
            suitable_users.append(i)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Функция, которая будет печатать читаемое имя переданной ей функции и значений аргументов.
def print_func_names(func, *args):
    func_name = func.__name__.replace("_", " ").title() # open_browser => "open browser" => "Open Browser"
    args_result = ", ".join([*args]) # ["https://companyname.com/login", "Register"] => "https://companyname.com/login, Register"
    result = f"{func_name} [{args_result}]"

    print(result)
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = None
    actual_result = print_func_names(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = None
    actual_result = print_func_names(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    actual_result = print_func_names(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
