from django.contrib import admin
from .models import Author, Editorial, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Editorial)
admin.site.register(Book)