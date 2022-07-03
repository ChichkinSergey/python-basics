# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__



def open_browser(browser_name):
    converter(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    converter(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    converter(go_to_companyname_homepage, page_url, button_text)

def converter(func, *args):
    function_name = func.__name__.replace("_", " ").title()
    print(f"Красивое имя функции: {function_name}")
    arguments = ""
    for argument in args:
        arguments = arguments + argument + " "
    print(f"Передаваемые аргументы: {arguments}")


open_browser("browser_name")
go_to_companyname_homepage("page_url")
find_registration_button_on_login_page("page_url", "button_text")