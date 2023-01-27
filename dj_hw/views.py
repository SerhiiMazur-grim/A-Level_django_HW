from django.http.response import HttpResponse
from django.http.request import HttpRequest


def home_page(request: HttpRequest):
    return HttpResponse('<h1>Домашня сторінка</h1>')


def num_progression(request: HttpRequest, start: int, count: int, step: int):
    my_list = [str(start)]
    for i in range(count):
        start += step
        my_list.append(str(start))
    return HttpResponse(f"<h1>{' '.join(my_list)}</h1>")


def fibonacci_of(request: HttpRequest, n: int):
    if n in {0, 1}:
        return HttpResponse(f"<h1>Число Фібоначчі з позицією {n} у послідовності: {n}</h1>")
    previous, fib_number = 0, 1
    for i in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number
    return HttpResponse(f"<h1>Число Фібоначчі з позицією {n} у послідовності: {fib_number}</h1>")


def greeting(request: HttpRequest, name: str):
    return HttpResponse(f'<h1>Вітаю {name}!</h1>')
