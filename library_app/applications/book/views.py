from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer


class ListAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.list_authors_by_country('China')
        return queryset
