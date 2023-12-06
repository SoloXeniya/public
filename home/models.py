from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to ="product/", verbose_name = "Изображения" )
    title = models.CharField(verbose_name = "Названия", max_length =100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"



