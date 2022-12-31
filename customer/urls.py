from django.urls import path
from . import views
app_name='customer'

urlpatterns = [
    path('',views.customer,name='customer'),
    path('customer_master',views.customer_master,name='customer_master')
]