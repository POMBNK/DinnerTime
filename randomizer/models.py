from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Menu(models.Model):
    class Categories(models.IntegerChoices):
        FIRST = 1, _("Первое")
        SECOND = 2, _("Второе")
        DRINKS = 3, _("Напитки")

    category = models.IntegerField(choices=Categories.choices, verbose_name="категории")
    label = models.CharField(max_length=50, verbose_name="Ресторан")
    food = models.CharField(max_length=50, verbose_name="Блюдо")

    def __str__(self):
        return f'{self.label} {self.category} {self.food}'
