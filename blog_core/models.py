from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=350, verbose_name='Заголовок')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    content = models.TextField(verbose_name='Контент')
    rating = models.IntegerField(verbose_name='Рейтинг')

    def __str__(self):
        return '{}: {}'.format(self.author, self.title)
