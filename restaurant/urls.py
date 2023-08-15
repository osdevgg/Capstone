from django.contrib import admin 
from django.urls import path 
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name = 'menuview'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name = 'singlemenuview'),
    path('api-token-auth/', obtain_auth_token),
]