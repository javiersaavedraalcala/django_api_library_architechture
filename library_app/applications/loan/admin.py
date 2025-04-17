from django.contrib import admin
from .models import Student, Loan, BookReturn

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name'
    )

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'student',
        'date'
    )

@admin.register(BookReturn)
class BookReturn(admin.ModelAdmin):
    list_display = (
        'loan',
        'date'
    )