from django.db import models

class Epoch(models.Model):
    name = models.CharField(max_length=2000, verbose_name="Эпоха")
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
    category = models.CharField(max_length=100, verbose_name="Категория")  # Языки, традиции, музыка
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='history/culture/', verbose_name="Фото", blank=True, null=True)
    audio_text = models.TextField(verbose_name="Текст к аудио", blank=True, null=True)
    audio = models.FileField(upload_to='history/audio/', verbose_name="Аудио", blank=True, null=True)
    youtube_link = models.URLField(verbose_name="Ссылка на YouTube", blank=True, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}"

class CultureImage(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='history/culture/', verbose_name="Фото")

