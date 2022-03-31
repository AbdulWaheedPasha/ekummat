# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Book, BookPDF

class BookPDFAdmin(admin.StackedInline):
    model = BookPDF

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookPDFAdmin]

@admin.register(BookPDF)
class BookPDFAdmin(admin.ModelAdmin):
    pass