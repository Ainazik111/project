from django.db import models

from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название приложения")
    description = models.TextField(verbose_name="Описание")
    playmarket_link = models.URLField(verbose_name="Ссылка на Play Market", blank=True, null=True)
    appstore_link = models.URLField(verbose_name="Ссылка на App Store", blank=True, null=True)
    image = models.ImageField(upload_to='guide/apps/', verbose_name="Иконка", blank=True, null=True)

    def __str__(self):
        return self.name


class InstagramAccount(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя аккаунта")
    link = models.URLField(verbose_name="Ссылка на Instagram")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.username


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сервиса")
    link = models.URLField(verbose_name="Ссылка", blank=True, null=True)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class EmergencyContact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название службы")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name} — {self.phone}"


class TravelTip(models.Model):
    title = models.CharField(max_length=150, verbose_name="Совет")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

