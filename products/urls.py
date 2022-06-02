from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('single_product/<int:id>', views.single_product, name='single_product'),
    path('search', views.search, name='search'),
]
