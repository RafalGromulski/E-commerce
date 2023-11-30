from django.urls import path, include
from rest_framework import routers

from .views import (
    WelcomingView,
    # ProductsListView,
    # ProductDetailsView,
    KategoriaProduktowViewSet,
    ProduktViewSet,
    ZamowienieViewSet,
    UserViewSet,
    # ProductDeleteView,
)
router = routers.DefaultRouter()
router.register(r"kategorie", KategoriaProduktowViewSet)
router.register(r"produkty", ProduktViewSet)
router.register(r"zamowienia", ZamowienieViewSet)
router.register(r"user", UserViewSet)


urlpatterns = [
    path("", WelcomingView.as_view(), name="welcoming_view"),
    # path("products_list/", ProductsListView.as_view(), name="products_list"),
    # path("product_details/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("api/produkty/<int:pk>/", ProductDeleteView.as_view()),
]
