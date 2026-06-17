from django.db import models

class Nature(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Статья / описание")
    image = models.ImageField(upload_to='nature/photos/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.title

