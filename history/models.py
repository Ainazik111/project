from django.db import models

class Epoch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Эпоха")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='history/epochs/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Событие")
    year = models.CharField(max_length=20, verbose_name="Год", blank=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='history/events/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.title


class Culture(models.Model):
    objects = None
    category = models.CharField(max_length=100, verbose_name="Категория")  # Языки, традиции, музыка
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='history/culture/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}"
