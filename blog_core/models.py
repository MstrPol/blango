from django.utils import timezone
from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=350, verbose_name='Заголовок')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    content = models.TextField(verbose_name='Контент')
    summary = models.TextField(max_length=500, verbose_name='Описание статьи')
    rating = models.IntegerField(verbose_name='Рейтинг')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликовано')
    date_publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    image = models.ImageField(
        default='/static/assets/images/blog/blog-post-thumb-1.jpg',
        upload_to='static/assets/images/blog/'
    )

    def __str__(self):
        return '{}: {}'.format(self.author, self.title)
