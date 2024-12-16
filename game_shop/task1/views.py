from django.shortcuts import render
from .models import Game, Buyer
from .forms import UserRegister
from django.db import models
from decimal import Decimal


menu = {'Навигационная страница': ["/"], 'Магазин': ["/games/"],
        'Корзина': ["/cart/"]}

context = {}


def info(request):
    context = {'base_name': 'Модуль 19. Django в Python.',
               'base_student': 'Студент: Крылов Эдуард Васильевич',
               'base_title': 'Навигационная страница'
               }
    return render(request, 'info/info.html', context)


def get_menu(request):
    context['base_title'] = 'Главная'
    context['menu'] = menu
    return render(request, 'fourth_task/menu.html', context)


def games(request):
    context['base_title'] = 'Игры'
    context['menu'] = menu

    content = Game.objects.all()
    # print(game)
    # content = {'games': game}
    # # print(content)
    context['games'] = content
    # # context['dascription'] = game.description
    print(context)
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    context['base_title'] = 'Корзина'
    context['base_cart'] = 'Извините, ваша корзина пуста'
    context['menu'] = menu
    return render(request, 'fourth_task/cart.html', context)


def sign_by_django(request):
    context = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            set_user = Buyer.objects.values_list('name', flat=True)

            if username in set_user:
                context['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                context['error'] = 'Пароли не совпадают'
            elif age <= 17:
                context['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                context['message'] = f'Пользователь, {username} успешно зарегистрирован!'

    context['form'] = form

    return render(request, 'fifth_task/registration_page.html', context)
