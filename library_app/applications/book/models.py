from django.db import models
from .managers import AuthorManager, BookManager


class Author(models.Model):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    country = models.CharField('País', max_length=30)

    objects = AuthorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Editorial(models.Model):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Titulo', max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='books')
    release = models.DateField('Publicación', blank=True, null=True)
    cover = models.ImageField('Portada', upload_to='book_stock', blank=True, null=True)  # Have to install Pillow

    objects = BookManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'{self.title} - {self.editorial}'
