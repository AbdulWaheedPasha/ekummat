# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    #Home page
    path('',views.quran_list_chapter, name='quran_list_chapter'),
    path('<int:chapter_id>/',views.quran_get_chapter, name='quran_get_chapter'),

    path('hadees_mainchapter',views.hadees_mainchapter, name='hadees_mainchapter'),
    # path('hadees_subchapter',views.hadees_subchapter, name='hadees_subchapter'),
    # path(r'^hadees_subchapter/(?P<value>\d+)/$',views.hadees_subchapter, name='hadees_subchapter'),
    path('hadees_subchapter/<int:chapter_no>/',views.hadees_subchapter, name='hadees_subchapter'),

    path('pdf_book_list',views.pdf_book_list, name='pdf_book_list'),

    # The Login page
    path('login', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
