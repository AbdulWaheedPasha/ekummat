# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Book, BookPDF, QuranChapterOld,HadithBook,HadithBookMainChapter,HadithBookSubChapter,HadithBookContent

@admin.register(HadithBook)
class HadithBookAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ()
    prepopulated_fields = {'slug': ('title',)}

@admin.register(HadithBookMainChapter)
class HadithBookMainChapterAdmin(admin.ModelAdmin):
    list_display = ("hadithbook","chapter_no","english_name","arabic_name")
    list_filter = ("hadithbook",)
    search_fields = ()

@admin.register(HadithBookSubChapter)
class HadithBookSubChapterAdmin(admin.ModelAdmin):
    list_display = ("hadith_book_main_chapter","sub_chapter_name",)
    list_filter = ("hadith_book_main_chapter",)
    search_fields = ()


@admin.register(QuranChapterOld)
class QuranChapterOldAdmin(admin.ModelAdmin):
    list_display = ("chapter_no","is_visible","created_at","updated_at")
    list_filter = ("chapter_no",)
    search_fields = ()


@admin.register(HadithBookContent)
class HadithBookContentAdmin(admin.ModelAdmin):
    list_display = ("hadith_book_sub_chapter",)
    list_filter = ("hadith_book_sub_chapter",)
    search_fields = ()


class BookPDFAdmin(admin.StackedInline):
    model = BookPDF
    list_filter = ("book",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookPDFAdmin]

@admin.register(BookPDF)
class BookPDFAdmin(admin.ModelAdmin):
    list_display = ("title","external_file_url",)
    list_filter = ("book",)