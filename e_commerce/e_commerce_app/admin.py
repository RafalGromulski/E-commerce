from django.contrib import admin

from .models import CategoryOfProduct, Product, Order

admin.site.register(CategoryOfProduct)
admin.site.register(Product)
admin.site.register(Order)
