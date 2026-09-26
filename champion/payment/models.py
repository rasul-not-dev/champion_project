from django.db import models

class Price(models.Model):
    price = models.PositiveIntegerField('цена в месяц')
    qr_code = models.ImageField('qr код', upload_to='qr_code/')

    class Meta():
        verbose_name = 'цена и qr код'
        verbose_name_plural = 'цена и qr код'

    def __str__(self):
        return str(self.price)

