from django.urls import path, register_converter
from . import views
from .converters import TwoDigitsNumber, ValidYear

app_name = 'book_app'


register_converter(TwoDigitsNumber, 'nn')
register_converter(ValidYear, 'aaaa')

urlpatterns = [
    path('api/author/list', views.ListAuthors.as_view()),
    # path('api/author/filter/<str:country>/', views.AuthorFilters.as_view())
    path('api/author/filter/<nn:age>/<country>', views.AuthorFilters.as_view()),
    path('api/book/after/<aaaa:year>', views.AfterBook.as_view()),
    path('api/book/bytitle', views.BooksByTitle.as_view()),
    path('api/book/filter', views.FilterBooks.as_view()),
    path('api/book/byauthor', views.BooksByAuthor.as_view()),
    path('api/author/detail/<pk>', views.DetailAuthor.as_view()),
    path('api/postman', views.Greetings.as_view()),
    path('api/editorial/save', views.SaveEditorial.as_view()),
    path('api/editorial/register', views.RegisterEditorial.as_view()),
]
