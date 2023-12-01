from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

from .models import CategoryOfProduct, Product, Order
from .permissions_mixins import StaffEditorPermissions, ActiveEditorPermissions
from .serializer import (
    UserSerializer,
    GroupSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
)


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryView(generics.ListAPIView):
    queryset = CategoryOfProduct.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "category", "description", "price"]
    ordering_fields = ["name", "category", "price"]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductCreateView(StaffEditorPermissions, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(StaffEditorPermissions, generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductDestroyView(StaffEditorPermissions, generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class OrderView(ActiveEditorPermissions, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
