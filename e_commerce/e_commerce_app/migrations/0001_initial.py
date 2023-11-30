# Generated by Django 4.2.7 on 2023-11-29 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriaProduktow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, verbose_name='Nazwa')),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres_dostawy', models.CharField(max_length=100, verbose_name='Adres dostawy')),
                ('lista_produktow', models.CharField(max_length=150, verbose_name='Lista produktów')),
                ('data_zamowienia', models.DateTimeField(verbose_name='Data zamówienia')),
                ('termin_platnosci', models.DateTimeField(verbose_name='Termin płatności')),
                ('sumaryczna_cena', models.FloatField(verbose_name='Sumaryczna cena')),
                ('klient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Klient')),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('opis', models.TextField(verbose_name='Opis')),
                ('cena', models.FloatField(verbose_name='Cena')),
                ('zdjecie', models.ImageField(upload_to='', verbose_name='Zdjęcie')),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce_app.kategoriaproduktow', verbose_name='Kategoria')),
            ],
        ),
    ]