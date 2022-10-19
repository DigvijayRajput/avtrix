from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    """
    Product models
    """
    name = models.CharField(max_length=20)
    order_date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.CharField(max_length=5)
    unit_price = models.CharField(max_length=5)

