from django.urls import path
from . import views
app_name='commen'

urlpatterns = [
    path('',views.commen,name='co_page'),
    path('commen_master',views.commen_master,name=''),
    path('customer_login',views.customer_login,name='customer-login'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('seller_login',views.seller_login,name='seller_login'),
    path('seller_register',views.seller_register,name='seller_register'),
]