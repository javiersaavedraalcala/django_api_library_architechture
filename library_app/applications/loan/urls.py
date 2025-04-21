from django.urls import path
from . import views

app_name = 'loan_app'

urlpatterns = [
    path('api/loan/create', views.RegisterLoan.as_view())
]