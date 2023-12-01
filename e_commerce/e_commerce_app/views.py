# from django.views.generic import TemplateView
# from rest_framework import authentication
from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets

from .models import CategoryOfProduct, Product, Order
from .permissions import IsStaffEditorPermissions, IsActiveEditorPermissions
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
    permission_classes = [permissions.AllowAny]


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "category", "description", "price"]
    ordering_fields = ["name", "category", "price"]
    permission_classes = [permissions.AllowAny]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.AllowAny]


class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class ProductDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class OrderView(generics.ListCreateAPIView):  # CreateAPIView
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, IsActiveEditorPermissions]
