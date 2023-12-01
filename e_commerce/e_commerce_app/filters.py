from django.db.models import Q
from django_filters import FilterSet, CharFilter

from .models import Product


class ProductsFilter(FilterSet):
    name = CharFilter(label="Nazwa...", method="nazwa_lookup_method")
    category = CharFilter(label="Kategoria...", method="kategoria_lookup_method")
    description = CharFilter(label="Opis...", method="opis_lookup_method")
    price = CharFilter(label="Cena...", method="cena_lookup_method")

    class Meta:
        model = Product
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
