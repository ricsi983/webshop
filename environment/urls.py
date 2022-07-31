from django.urls import path
from products.infrastructure.controller import ProductController
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', ProductController.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
