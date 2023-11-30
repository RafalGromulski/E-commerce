from django.db import models
from django.contrib.auth.models import User


class KategoriaProduktow(models.Model):
    nazwa = models.CharField(verbose_name="Nazwa", max_length=50)

    def __str__(self):
        return str(self.nazwa)


class Produkt(models.Model):
    nazwa = models.CharField(verbose_name="Nazwa", max_length=100)
    opis = models.TextField(verbose_name="Opis")
    cena = models.FloatField(verbose_name="Cena")
    kategoria = models.ForeignKey(KategoriaProduktow, verbose_name="Kategoria", on_delete=models.CASCADE)
    zdjecie = models.ImageField(verbose_name="Zdjęcie")

    def __str__(self):
        return str(self.nazwa)


class Zamowienie(models.Model):
    klient = models.OneToOneField(User, verbose_name="Klient", on_delete=models.CASCADE)  # czy inny model???
    adres_dostawy = models.CharField(verbose_name="Adres dostawy", max_length=100)
    lista_produktow = models.CharField(verbose_name="Lista produktów", max_length=150)
    data_zamowienia = models.DateTimeField(verbose_name="Data zamówienia")
    termin_platnosci = models.DateTimeField(verbose_name="Termin płatności")
    sumaryczna_cena = models.FloatField(verbose_name="Sumaryczna cena")

    def __str__(self):
        return str(self.klient)
