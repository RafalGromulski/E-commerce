from django.contrib.auth.models import User
from rest_framework import serializers

from .models import KategoriaProduktow, Produkt, Zamowienie


class KategoriaProduktowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KategoriaProduktow
        fields = "__all__"


class ProduktSerializer(serializers.HyperlinkedModelSerializer):
    kategoria = serializers.StringRelatedField(many=False)

    class Meta:
        model = Produkt
        fields = "__all__"


class ZamowienieSerializer(serializers.HyperlinkedModelSerializer):
    klient = serializers.StringRelatedField(many=False)

    class Meta:
        model = Zamowienie
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = "__all__"
