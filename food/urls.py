from importlib.resources import path
from unicodedata import name
from unittest.mock import patch
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail')
]
