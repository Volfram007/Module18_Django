from django.shortcuts import render


def index3(request):
    context = {
        'shop_title': 'Dj Shop',
        'title': 'Главная страница',
        'links': [
            {'name': 'К заданиям', 'url': 'index'},
            {'name': 'Магазин', 'url': 'shop3'},
            {'name': 'Корзина', 'url': 'cart3'},
        ]
    }
    return render(request, 'third_task/index.html', context)


def shop3(request):
    context = {
        'title': 'Магазин',
        'items': {
            'item1': 'Петька и Василий Иванович',
            'item2': 'Братья Пилоты',
            'item3': 'ГЭГ',
        },
    }
    return render(request, 'third_task/shop.html', context)


# Страница Корзина
def cart3(request):
    context = {
        'title': 'Корзина',
        'cart_info': 'Ваша корзина пуста, но это временно! {Тут смайл ёпта}',
    }
    return render(request, 'third_task/cart.html', context)
