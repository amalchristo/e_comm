from django.urls import path
from . import views
app_name='comm_admin'

urlpatterns = [
    path('',views.index,name='co_admin'),
    path('layouts-without-menu',views.layouts_without_menu,name='layouts-without-menu'),
]