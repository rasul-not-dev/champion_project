from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО тренера")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='trainers/', verbose_name="Фотография")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class Contacts(models.Model):
    post = models.CharField(max_length=50, verbose_name='должность')
    name = models.CharField(max_length=50, verbose_name='имя')
    number = PhoneNumberField(region='RU', verbose_name='номер')

    def __str__(self):
        return self.post
    
    class Meta():
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class GymGallery(models.Model):
    photo = models.ImageField('фото', upload_to='gym_gallery')

    class Meta():
        verbose_name = "Фотография зала"
        verbose_name_plural = "Фотографии зала"