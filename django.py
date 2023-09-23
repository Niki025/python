from django.db import models


class DataFields(models.Model):
    created_at = models.DtaTimedField(auto_now_add=True)
    updated_at = models.DataTimedField(auto_now=true)

    class Meta:
        abstract = True


class Product(DataFields):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Category(DataFields):
    name = models.CharField(max_length=100)
