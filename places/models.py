from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255,verbose_name= "Название места")
    title = models.CharField(max_length=255, verbose_name= "Краткое описание")
    is_pamyatnik = models.BooleanField(default=False, verbose_name= "Это памятник ?")
    image_1 = models.ImageField(upload_to='place/', verbose_name= "Изображение 1")
    image_2 = models.ImageField(upload_to='place/', verbose_name= "Изображение 2")
    image_3 = models.ImageField(upload_to='place/', verbose_name= "Изображение 3")
    text_1 = models.TextField( verbose_name= "Текст описания 1")
    text_2 = models.TextField( verbose_name= "Текст описания 2")
    text_3 = models.TextField( verbose_name= "Текст описания 3")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.is_pamyatnik:
            return f'/places/{self.id}/'
        if not self.is_pamyatnik:
            return f'/places/{self.id}/'
            
    class Meta:
        verbose_name= "Название места"
        verbose_name= "Краткое описание"
        verbose_name= "Это памятник ?"
        verbose_name= "Изображение 1"
        verbose_name= "Изображение 2"
        verbose_name= "Изображение 3"
        verbose_name= "Текст описания 1"
        verbose_name= "Текст описания 2"
        verbose_name= "Текст описания 3"
        verbose_name= "Место"
        verbose_name_plural= "Места"
        