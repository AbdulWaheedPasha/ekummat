# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pyexpat import model
from statistics import mode
from turtle import title, update
from venv import create
from django.db import models
from django.contrib.auth.models import User

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
    file_url = models.FileField(upload_to=BookPDF_upload_location, null = False, blank = False)
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