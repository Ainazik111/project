from django.db import models

from django.db import models

class Food(models.Model):
    CATEGORY_CHOICES = [
        ('main', 'Основные блюда'),
        ('flour', 'Мучное'),
        ('delicacy', 'Деликатесы'),
        ('dessert', 'Лакомства'),
        ('drink', 'Напитки'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='food/photos/', verbose_name="Фото", blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"



class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название напитка")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='food/drinks/', verbose_name="Фото напитка", blank=True, null=True)

    def __str__(self):
        return self.name

