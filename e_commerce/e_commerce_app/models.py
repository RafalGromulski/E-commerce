from django.contrib.auth.models import User
from django.db import models


class CategoryOfProduct(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=50)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=100)
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(verbose_name="Cena", max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        CategoryOfProduct, verbose_name="Kategoria", on_delete=models.CASCADE
    )
    picture = models.ImageField(verbose_name="Zdjęcie")

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    customer = models.OneToOneField(
        User, verbose_name="Klient", on_delete=models.CASCADE
    )
    delivery_address = models.CharField(verbose_name="Adres dostawy", max_length=100)
    products_list = models.CharField(verbose_name="Lista produktów", max_length=150)
    date_order = models.DateTimeField(verbose_name="Data zamówienia")
    date_payment = models.DateTimeField(verbose_name="Termin płatności")
    total_price = models.DecimalField(
        verbose_name="Sumaryczna cena", max_digits=8, decimal_places=2
    )

    def __str__(self):
        return str(self.customer)
