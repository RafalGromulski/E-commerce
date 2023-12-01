from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import CategoryOfProduct, Product, Order


class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.StringRelatedField(many=False)

    class Meta:
        model = Group
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryOfProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)  # do wyjaśnienia - do wyboru wszyscy użytkownicy

    class Meta:
        model = Order
        fields = "__all__"
