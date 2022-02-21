from django.db import models
from django.conf import settings

from news.models import New
from places.models import Place


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name= "Пользователь"
    )
    text = models.TextField(verbose_name= "Текст комментария")
    date_created = models.DateTimeField(auto_now_add=True ,verbose_name= "Дата создания")
    post = models.ForeignKey(New, on_delete=models.CASCADE, verbose_name= "Пост")
    check = models.BooleanField(verbose_name= "Проверено ?")

    def __str__(self):
        return f'{self.user.firstname} комментарий  {self.date_created}'
    
    class Meta:
        unique_together = ['user', 'text', 'post']
        verbose_name = "Место"
        verbose_name_plural = "Места"
        verbose_name= "Пользователь"
        verbose_name_plural= "Пользователи"
        verbose_name= "Текст комментария"
        verbose_name= "дата создания"
        verbose_name= "Проверено ?"
        verbose_name= "Комментарий"
        verbose_name_plural= "Комментарии"


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,verbose_name= "Пользователь"
    )
    text = models.TextField(verbose_name= "Текст отзыва")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name= "Дата создания")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")
    check = models.BooleanField(verbose_name= "Проверено ?")
    def __str__(self):
        return f'{self.user.firstname} отзыв  {self.date_created}'

    class Meta:
        unique_together = ['user', 'text', 'place']
        verbose_name = "Место"
        verbose_name_plural = "Места"
        verbose_name= "Пользователь"
        verbose_name_plural= "Пользователи"
        verbose_name= "Текст отзыва"
        verbose_name= "дата создания"
        verbose_name= "Проверено ?"
        verbose_name= "Отзыв"
        verbose_name_plural= "Отзывы"
    



