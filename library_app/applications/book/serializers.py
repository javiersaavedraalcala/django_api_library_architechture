from rest_framework import serializers, pagination
from .models import Author, Book, Editorial


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 50


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'country')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = (
            'name',
        )
