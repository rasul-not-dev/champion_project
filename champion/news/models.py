from django.db import models
from pytils.translit import slugify

class News(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    slug = models.SlugField("Слаг", max_length=100, unique=True, blank=True)
    image = models.ImageField("Картинка", upload_to='events/')
    content = models.TextField("Описание")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "news"
            slug = base_slug
            counter = 1
            
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = slug
            
        super().save(*args, **kwargs)

    
    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

    def __str__(self):
        return self.title