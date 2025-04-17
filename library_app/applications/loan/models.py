from django.db import models
from ..book.models import Book


# Create your models here.
class Student(models.Model):
    DNI = models.CharField('DNI', max_length=16)
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f'{self.DNI} - {self.name} {self.last_name}'


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Libro')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')
    description = models.CharField('Descripción', max_length=100, blank=True)
    date = models.DateField('Fecha prestamo', blank=True, null=True)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return f'{self.book.title} {self.date}'


class BookReturn(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='Prestamo')
    date = models.DateField('Fecha devolución', blank=True, null=True)

    class Meta:
        verbose_name = 'Devolución'
        verbose_name_plural = "Devoluciones"

    def __str__(self):
        return self.loan.book.title
