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
    url_retrieve = serializers.HyperlinkedIdentityField(
        view_name="product-retrieve", lookup_field="pk"
    )
    url_create = serializers.HyperlinkedIdentityField(
        view_name="product-create", lookup_field="pk"
    )
    url_update = serializers.HyperlinkedIdentityField(
        view_name="product-update", lookup_field="pk"
    )
    url_delete = serializers.HyperlinkedIdentityField(
        view_name="product-delete", lookup_field="pk"
    )
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "url_retrieve",
            "url_create",
            "url_update",
            "url_delete",
            "name",
            "description",
            "price",
            "category",
            "picture",
        ]


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = "__all__"
