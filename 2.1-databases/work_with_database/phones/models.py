from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Картинка')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)
