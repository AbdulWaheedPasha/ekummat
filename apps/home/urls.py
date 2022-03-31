# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    #Home page
    path('',views.home, name='homenew'),
    
    path('hadees_mainchapter',views.hadees_mainchapter, name='hadees_mainchapter'),
    path('hadees_subchapter',views.hadees_subchapter, name='hadees_subchapter'),
    
    path('pdf_book_list',views.pdf_book_list, name='pdf_book_list'),

    # The Login page
    path('login', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
