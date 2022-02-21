from django.db import models

class New(models.Model):
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    title = models.CharField(max_length=200,verbose_name = "Заголовок")
    text_1 = models.TextField(verbose_name= "Информация")
    quote = models.CharField(max_length=200, verbose_name= "Цитата")
    text_2 = models.TextField(verbose_name= "Информация")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name= "Дата создания")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}/'

    class Meta:
        verbose_name= "Дата создания"
        verbose_name = "Заголовок"
        verbose_name_plural= "Новости"
        verbose_name = "Изображение"
        verbose_name= "Информация"
        verbose_name= "Цитата"
        verbose_name= "Новость"
        

       
