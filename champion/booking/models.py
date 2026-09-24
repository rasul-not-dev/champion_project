from django.db import models

class Booking(models.Model):
    image = models.ImageField('аватарка', upload_to='booking/')
    name = models.CharField('имя', max_length=50)
    number = models.CharField('номер', max_length=15)
    adres = models.CharField('адрес', max_length=50)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

class BookingMedia(models.Model):
    name = models.CharField('имя', max_length=50)
    link = models.CharField('ссылка', max_length=500)
    icon = models.CharField('иконка', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'соцсеть'
        verbose_name_plural = 'соцсети'

class BookingNumbers(models.Model):
    name = models.CharField('фио теренера')
    number = models.CharField('номер тренера')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'номер тренера'
        verbose_name_plural = 'номера тренеров'