from django.urls import path
# from rest_framework import routers

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

# router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)
# router.register(r"groups", GroupViewSet)
# router.register(r"categories", CategoryViewSet)
# router.register(r"products", ProductViewSet)
# router.register(r"orders", OrderViewSet)


urlpatterns = [
    # path("", include(router.urls)),  # do weryfikacji
    path("users/", UserView.as_view()),
    path("groups/", GroupView.as_view()),
    path("categories/", CategoryView.as_view()),
    path("orders/", OrderView.as_view()),
    # path("orders/<int:pk>/", xxxx.as_view()),
    path("products/", ProductView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<int:pk>/create/", ProductCreateView.as_view()),
    path("products/<int:pk>/update/", ProductUpdateView.as_view()),
    path("products/<int:pk>/delete/", ProductDestroyView.as_view()),
]

# urlpatterns += router.urls
