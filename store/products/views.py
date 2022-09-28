from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title' : 'Store',
        'header' : 'Добро пожаловать!',
        'username' : 'Болат Сареев',
        'products' : [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ]
    }
    return render(request, 'products/test-context.html', context)
