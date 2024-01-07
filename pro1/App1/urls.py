from django.urls import path
from .views import index,addItem

urlpatterns = [  
    path('', index, name='index'),
    path('add_item/', addItem, name='add_item'),
]