from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Reviews(models.Model):
    name = models.CharField('имя', max_length=25)
    comment = models.TextField('комментарий', max_length=800)
    rating = models.IntegerField(
        'рейтинг', 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField('время', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.rating}★'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'