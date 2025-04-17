from django.db import models


class AuthorManager(models.Manager):
    def list_authors_by_country(self, country):
        return self.filter(
            country = country
        )
