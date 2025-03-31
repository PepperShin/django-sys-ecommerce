from django.db import models

# Create your models here.
# dev_3


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)  # 9999.99
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="upload/product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # dev_6
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
