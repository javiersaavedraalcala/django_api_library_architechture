from django.db import models


class AuthorManager(models.Manager):
    def list_authors_by_country(self, country):
        return self.filter(
            country=country
        )


class BookManager(models.Manager):
    def list_after_books(self, year):
        return self.filter(
            release__year__gt=year
        )

    def books_by_title(self, kword):
        return self.filter(
            title__icontains=kword
        ).order_by('title')

    def books_filter(self, title, year):
        return self.filter(
            title__icontains=title,
            release__year__gt=year
        )

    def books_by_author(self, author_name):
        return self.filter(
            author__name__icontains = author_name
        ).order_by('release')