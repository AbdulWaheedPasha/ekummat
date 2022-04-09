# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from operator import mod
from pyexpat import model
from statistics import mode
from turtle import title, update
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuid import uuid4

def generateUUID():
    return str(uuid4())

from tinymce.models import HTMLField


# Create your models here.
def BookPDF_upload_location(instance, filename):
    model_name = instance.book.title.lower().replace(" ", "-")
    file_name = filename.lower().replace(" ", "-")
    return "book/{}/{}".format(model_name, file_name)


class Book(models.Model):
    title = models.TextField(blank=False,null=False)
    volumes = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title

class BookPDF(models.Model):
    # book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, related_name='book')
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True, blank=True,)
    title = models.TextField(blank=False,null=False)
    total_pages = models.TextField(blank=True,null=True)
    file_url = models.FileField(upload_to=BookPDF_upload_location, null = True, blank = True)
    external_file_url = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title


class QuranChapterOld(models.Model):
    chapter_no = models.IntegerField(null=False,blank=False)
    chapter_content = HTMLField(null=False,blank=False)
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chapter_no)


#Mishkatul Masabeeh
class HadithBook(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)


#Mishkatul Masabeeh #Faith (main chapter heading)
class HadithBookMainChapter(models.Model):
    hadithbook = models.ForeignKey(HadithBook,on_delete=models.SET_NULL,null=True)
    chapter_no = models.IntegerField(max_length=3)
    english_name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.english_name

#Mishkatul Masabeeh -> #Faith -> #sub chapters
class HadithBookSubChapter(models.Model):
    hadith_book_main_chapter = models.ForeignKey(HadithBookMainChapter,on_delete=models.SET_NULL,null=True)
    sub_chapter_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.hadith_book_main_chapter} - {self.sub_chapter_name}"


HADITHGRADE = [
    ("Muttafaqun 'alayh","Muttafaqun 'alayh"),
    ("Sahih","Sahih"),
    ("Hasan","Hasan"),
    ("Zaeef","Zaeef"),
]
#Mishkatul Masabeeh -> #Faith -> #sub chapters -> content
class HadithBookContent(models.Model):
    hadith_book_sub_chapter = models.ForeignKey(HadithBookSubChapter,on_delete=models.SET_NULL,null=True)
    sr_no = models.IntegerField(max_length=3)
    arabic_content = models.TextField()
    roman_urdu_content = models.TextField()
    hindi_content = models.TextField()
    reference_field = models.TextField()
    grade = models.CharField(choices=HADITHGRADE,default="Sahih", max_length=50)

    def __str__(self):
        return f"{self.hadith_book_sub_chapter}"

