from django.urls import path
from .views import Transaction_list, User_Monthly_list

app_name = 'credit_api'
urlpatterns = [
    path('transaction', Transaction_list),
    path('useramount', User_Monthly_list)
]
