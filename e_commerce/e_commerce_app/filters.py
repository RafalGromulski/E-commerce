from django.db.models import Q
from django_filters import FilterSet, CharFilter

from .models import Produkt


class ProductsFilter(FilterSet):
    nazwa = CharFilter(label="Nazwa...", method="nazwa_lookup_method")
    kategoria = CharFilter(label="Kategoria...", method="kategoria_lookup_method")
    opis = CharFilter(label="Opis...", method="opis_lookup_method")
    cena = CharFilter(label="Cena...", method="cena_lookup_method")

    class Meta:
        model = Produkt
        fields = []

    @classmethod
    def nazwa_lookup_method(cls, queryset, name, value):
        return queryset.filter(Q(nazwa__icontains=value))

    @classmethod
    def kategoria_lookup_method(cls, queryset, name, value):
        return queryset.filter(Q(kategoria__icontains=value))

    @classmethod
    def opis_lookup_method(cls, queryset, name, value):
        return queryset.filter(Q(opis__icontains=value))

    @classmethod
    def cena_lookup_method(cls, queryset, name, value):
        return queryset.filter(Q(cena__icontains=value))
