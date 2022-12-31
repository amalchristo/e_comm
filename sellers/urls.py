from django.urls import path
from . import views
app_name='sellers'

urlpatterns = [
    path('',views.sellers,name='sellers'),
]