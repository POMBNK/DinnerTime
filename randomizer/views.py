from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse
import random


# Create your views here.


def homepage(request):
    return render(request, 'randomizer/home.html')


def rest_choice(request):
    restoraunts = ['BurgerKing', 'Сытопьяно', 'Теремок', 'Домой', 'KFC', 'Отсосать бомжу']
    random_key = random.choice(restoraunts)
    choose = {'restik': random_key}
    match random_key:
        case "Теремок":
            random_menu = Menu.objects.filter(label="Теремок")
            random1 = random.choice(list(random_menu.filter(category=1)))
            random2 = random.choice(list(random_menu.filter(category=2)))
            random3 = random.choice(list(random_menu.filter(category=3)))
            choose['food1'] = random1.food
            choose['food2'] = random2.food
            choose['food3'] = random3.food
            return render(request, 'randomizer/choice.html', choose)
        case "Сытопьяно":
            random_menu = Menu.objects.filter(label="Сыто-пьяно")
            random1 = random.choice(list(random_menu.filter(category=1)))
            random2 = random.choice(list(random_menu.filter(category=2)))
            random3 = random.choice(list(random_menu.filter(category=3)))
            choose['food1'] = random1.food
            choose['food2'] = random2.food
            choose['food3'] = random3.food
            return render(request, 'randomizer/choice.html', choose)
        case "KFC":
            random_menu = Menu.objects.filter(label="KFC")
            random1 = random.choice(list(random_menu.filter(category=1)))
            random2 = random.choice(list(random_menu.filter(category=2)))
            random3 = random.choice(list(random_menu.filter(category=3)))
            choose['food1'] = random1.food
            choose['food2'] = random2.food
            choose['food3'] = random3.food
            return render(request, 'randomizer/choice.html', choose)
        case "BurgerKing":
            random_menu = Menu.objects.filter(label="Burger King")
            random1 = random.choice(list(random_menu.filter(category=1)))
            random2 = random.choice(list(random_menu.filter(category=2)))
            random3 = random.choice(list(random_menu.filter(category=3)))
            choose['food1'] = random1.food
            if "Комбо" in choose['food1']:
                choose['food2'] = "Комбо достаточно :)"
                choose['food3'] = random3.food
            else:
                choose['food2'] = random2.food
                choose['food3'] = random3.food
            return render(request, 'randomizer/choice.html', choose)
        case "Домой":
            choose['food1'] = "Тебе выпал счастливый билет"
            return render(request, 'randomizer/choice.html', choose)
        case "Отсосать бомжу":
            choose['food1'] = "Тебе выпал несчастливый билет"
            return render(request, 'randomizer/choice.html', choose)




