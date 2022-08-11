from django.urls import path, re_path
from drf_yasg import openapi
from rest_framework import permissions

from products.infrastructure.controller import ProductController
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('products/', ProductController.as_view()),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns = format_suffix_patterns(urlpatterns)
