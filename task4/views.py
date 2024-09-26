from django.shortcuts import render


def index4(request):
    context = {
        'shop_title': 'Dj Shop',
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/index.html', context)


def shop4(request):
    context = {
        'games': ['The Settlers', 'Doom', 'Tetris']
    }
    return render(request, 'fourth_task/shop.html', context)


# Страница Корзина
def cart4(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'fourth_task/cart.html', context)
