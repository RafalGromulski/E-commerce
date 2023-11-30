from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.contrib.auth.models import User
from rest_framework import generics
from .filters import ProductsFilter
from .models import KategoriaProduktow, Produkt, Zamowienie
from .serializer import (
    KategoriaProduktowSerializer,
    ProduktSerializer,
    ZamowienieSerializer,
    UserSerializer,
)


class WelcomingView(TemplateView):
    template_name = "welcoming_view.html"


# class ProductsListView(View):
#     model = Produkt
#     template_name = "products_list.html"
#
#     def get(self, request):
#         products = self.model.objects.all()
#         my_filter = ProductsFilter(request.GET, queryset=products)
#         products = my_filter.qs
#
#         context = {
#             "products": products,
#             "my_filter": my_filter,
#         }
#
#         return render(request, self.template_name, context)


# class ProductDetailsView(TemplateView):
#     model = Produkt
#     template_name = "product_details.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["product"] = self.model.objects.get(id=kwargs["pk"])
#
#         return context


class KategoriaProduktowViewSet(ModelViewSet):
    queryset = KategoriaProduktow.objects.all()
    serializer_class = KategoriaProduktowSerializer


class ProduktViewSet(ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["nazwa", "kategoria", "opis", "cena"]
    ordering_fields = ["nazwa", "kategoria", "cena"]


class ZamowienieViewSet(ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer



# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Produkt.objects.all()
#     serializer_class = ProduktSerializer
