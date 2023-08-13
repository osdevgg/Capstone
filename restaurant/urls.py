from django.contrib import admin 
from django.urls import path 
from .views import index, MenuItemView, SingleMenuItemView

  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]