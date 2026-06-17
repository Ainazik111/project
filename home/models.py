from django.db import models

class HomeInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='home/photos/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.title


class Population(models.Model):
    number = models.CharField(max_length=50, verbose_name="Население")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.number


class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Язык")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name


class People(models.Model):
    description = models.TextField(verbose_name="Описание о народе")

    def __str__(self):
        return "Описание о народе"


class NationalGame(models.Model):
    name = models.CharField(max_length=100, verbose_name="Национальная игра")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name


class MusicalInstrument(models.Model):
    name = models.CharField(max_length=100, verbose_name="Музыкальный инструмент")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

