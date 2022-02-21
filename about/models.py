from django.db import models

class About(models.Model):
    about_image = models.ImageField(upload_to='about/',  verbose_name= "Изображение библиотеки")
    text_about = models.TextField(  verbose_name= "Дополнительный текст")
    title_about = models.TextField(   verbose_name= "Основной текст")
    text_1 = models.TextField(  verbose_name= "История библиотеки 1")
    text_2 = models.TextField( verbose_name= "История библиотеки 2")
    text_3 = models.TextField(  verbose_name= "История библиотеки 3")
    image_1 = models.ImageField(upload_to='about/',  verbose_name= "Изображение 1")
    image_2 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 2")
    image_3 = models.ImageField(upload_to='about',   verbose_name= "Изображение 3")
    image_4 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 4")
    image_5 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 5")
    image_6 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 6")
    image_7 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 7")
    image_8 = models.ImageField(upload_to='about/',   verbose_name= "Изображение 8")
    
    def __str__(self):
        return self.title_about

    def get_image_urls(self):
        images = [self.image_1,self.image_2,self.image_3,self.image_4,self.image_5,self.image_6,self.image_7,self.image_8]
        urls = [image.url for image in images]
        return urls
    class Meta:
    
        verbose_name= "Изображение библиотеки"
        verbose_name= "Дополнительный текст"
        verbose_name= "Основной текст"
        verbose_name= "История библиотеки 1"
        verbose_name= "История библиотеки 2"
        verbose_name= "История библиотеки 3"
        verbose_name= "Изображение 1"
        verbose_name= "Изображение 2"
        verbose_name= "Изображение 3"
        verbose_name= "Изображение 4"
        verbose_name= "Изображение 5"
        verbose_name= "Изображение 6"
        verbose_name= "Изображение 7"
        verbose_name= "Изображение 8"
        verbose_name = "О нас"
        verbose_name_plural= "О нас"

class GaleryPhoto(models.Model):
    image = models.ImageField(upload_to='galery/', verbose_name= "Изображение")

    class Meta:
    
        verbose_name= "Изображение"
        verbose_name = "Фотография из галереи"
        verbose_name_plural= "Фотографии из галереи"
       