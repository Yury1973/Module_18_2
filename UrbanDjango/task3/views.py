from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page.html')


def games(request):
    title = 'Мой сайт'
    head = 'Игры'
    game1 = 'Atomic Hart'
    game2 = 'Cyberpunk 2077'
    game3 = 'Pay Day 2'
    context = {
        'title': title,
        'head': head,
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
