from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response

from .models import Author, Book, Editorial
from .serializers import AuthorSerializer, BookSerializer, PaginationSerializer, EditorialSerializer


class ListAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        print('*****')
        print(request.path)
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Author.objects.list_authors_by_country('China')
        return queryset


class AuthorFilters(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        print('*****')
        age = self.kwargs['age']
        country = self.kwargs['country']
        print(country)
        queryset = Author.objects.list_authors_by_country(country)
        return queryset


class AfterBook(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = Book.objects.list_after_books(year)
        return queryset


class BooksByTitle(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        queryset = Book.objects.books_by_title(kword)
        return queryset


class FilterBooks(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        year = self.request.query_params.get('year', 1990)
        queryset = Book.objects.books_filter(title, year)
        return queryset


class BooksByAuthor(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = PaginationSerializer

    def get_queryset(self):
        author_name = self.request.query_params.get('author_name', '')
        queryset = Book.objects.books_by_author(author_name)
        return queryset


class DetailAuthor(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class Greetings(views.APIView):
    def get(self, request):
        print('------------------')
        print(request)
        return Response({'status': 'OK GET'})

    def post(self, request):
        print('------------------')
        print(request)
        print(self.request.data)
        print('****************')
        print(request.data['title'])  # Accediendo a los valores de la data
        return Response({'status': 'OK POST'})

    def delete(self, request):
        print('--------------------')
        print(request)
        return Response({'status': 'OK DELETE'})


# Esta forma es mala, no es la ideal
class SaveEditorial(views.APIView):
    def post(self, request):
        print('------------------')
        print(request.data)
        print('****************')
        name = request.data['name']  # Accediendo a los valores de la data
        Editorial.objects.create(
            name=name
        )
        return Response({'status': 'OK POST'})


class RegisterEditorial(generics.CreateAPIView):
    serializer_class = EditorialSerializer
    queryset = Editorial.objects.all()


