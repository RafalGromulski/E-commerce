from django.urls import path

from .views import (
    UserView,
    GroupView,
    CategoryView,
    ProductView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDestroyView,
    OrderView,
)

urlpatterns = [
    path("users/", UserView.as_view(), name="user-list"),
    path("groups/", GroupView.as_view(), name="group-list"),
    path("categories/", CategoryView.as_view(), name="category-list"),
    path("orders/", OrderView.as_view(), name="order-list"),
    path("products/", ProductView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-retrieve"),
    path(
        "products/<int:pk>/create/", ProductCreateView.as_view(), name="product-create"
    ),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDestroyView.as_view(), name="product-delete"
    ),
]
