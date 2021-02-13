from django.db import models


class Picture(models.Model):
    image = models.ImageField('Файл', upload_to='images/', blank=True)
    link = models.URLField('Ссылка', max_length=200, blank=True)
    width = models.IntegerField('Ширина', blank=True)
    height = models.IntegerField('Высота', blank=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True,
                                   db_index=True, )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-created']

    def __str__(self):
        name = str(self.image).split('/')[-1]
        return name
