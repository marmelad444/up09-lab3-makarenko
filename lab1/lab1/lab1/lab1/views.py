from django.shortcuts import render
# Импорт функции `render` из модуля `django.shortcuts`.
# Эта функция используется для отображения HTML-шаблонов
# с передачей в них данных.

def about(req):
    # Определение функции `about`, которая принимает один параметр `req`.
    # Обычно `req` — это объект запроса (request), передаваемый Django при вызове функции.

    return render(req, "about.html")
    # Функция `render` генерирует HTTP-ответ с указанным HTML-шаблоном.
    # Здесь `req` — объект запроса, передаваемый для обработки, а `"about.html"` —
    # имя файла HTML-шаблона, который будет отображён пользователю.
    # Если требуется передать данные в шаблон, их можно указать третьим параметром
    # в виде словаря (например, `{"key": "value"}`).
def index(req):
    return render(req, "index.html")

