from django.db import models

from django.db import models

class NatureArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    main_description = models.TextField(verbose_name="Общее описание")

    def __str__(self):
        return self.title


class NatureContent(models.Model):
    article = models.ForeignKey(NatureArticle, on_delete=models.CASCADE, related_name="contents")
    image = models.ImageField(upload_to='nature/photos/', verbose_name="Фото", blank=True, null=True)
    text = models.TextField(verbose_name="Текст", blank=True, null=True)

    def __str__(self):
        return f"Блок для {self.article.title}"

