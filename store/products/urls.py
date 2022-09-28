from django.urls import path
from .views import index, products, test_context

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('test-context/', test_context, name='test_context'),
]