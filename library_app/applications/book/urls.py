from django.urls import path
from . import views

app_name = 'book_app'


urlpatterns = [
    path('api/author/list', views.ListAuthors.as_view())
]