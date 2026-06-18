from django.db import models

class BishkekIntro(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='bishkek/photos/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.title


class Place(models.Model):
    CATEGORY_CHOICES = [
        ('park', 'Парк'),
        ('museum', 'Музей'),
        ('mall', 'Торговый центр'),
        ('bazaar', 'Базар'),
        ('restaurant', 'Ресторан'),
        ('attraction', 'Достопримечательность'),
    ]

    title = models.CharField('Название', max_length=200)
    category = models.CharField(
        'Категория',
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField('Описание')
    image = models.ImageField(
        'Фотография',
        upload_to="media",
        blank=True,
        null=True
    )
    address = models.CharField(
        'Адрес',
        max_length=300,
        blank=True
    )
    google_maps = models.URLField(
        'Google Maps',
        blank=True
    )
    website = models.URLField(
        'Сайт',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'