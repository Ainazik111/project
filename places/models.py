from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название места")
    region = models.CharField(max_length=100, verbose_name="Регион / область")
    description = models.TextField(verbose_name="Краткое описание")
    image = models.ImageField(upload_to='places/photos/', verbose_name="Фото", blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('bazaar', 'Базар'),
            ('nature', 'Природное место'),
            ('sight', 'Достопримечательность'),
            ('other', 'Другое')
        ],
        verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.name} ({self.region})"

