from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='food/dishes/', verbose_name="Фото блюда", blank=True, null=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название напитка")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='food/drinks/', verbose_name="Фото напитка", blank=True, null=True)

    def __str__(self):
        return self.name

