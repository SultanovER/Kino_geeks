from django.db import models

class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    name = models.CharField(max_length=255, verbose_name='Название')
    director = models.CharField(max_length=100, verbose_name='Режиссёр')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title
