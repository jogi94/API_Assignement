from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=255, help_text="Enter Product Name.")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Product'

    def __str__(self):
        return self.name

