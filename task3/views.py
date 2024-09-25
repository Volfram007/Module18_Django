from django.shortcuts import render

def index3(request):
    context = {
        'shop_title': 'Dj Shop',
        'title': 'Главная страница',
        'links': [
            {'name': 'Главная', 'url': 'index'},
            {'name': 'Магазин', 'url': 'shop'},
            {'name': 'Корзина', 'url': 'cart'},
        ]
    }
    return render(request, 'third_task/index-shop.html', context)

def shop(request):
    context = {
        'title': 'Магазин',
        'items': {
            'item1': 'Петька и Василий Иванович',
            'item2': 'Братья Пилоты',
            'item3': 'ГЭГ',
        },
        'links': [
            {'name': 'Главная', 'url': 'index'},
            {'name': 'Магазин', 'url': 'shop'},
            {'name': 'Корзина', 'url': 'cart'},
        ]
    }
    return render(request, 'third_task/shop.html', context)

# Страница Корзина
def cart(request):
    context = {
        'title': 'Корзина',
        'cart_info': 'Ваша корзина пуста, но это временно! {Тут смайл ёпта}',
        'links': [
            {'name': 'Главная', 'url': 'index'},
            {'name': 'Магазин', 'url': 'shop'},
            {'name': 'Корзина', 'url': 'cart'},
        ]
    }
    return render(request, 'third_task/cart.html', context)