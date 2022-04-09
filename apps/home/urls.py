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

    path('mishkat-al-masabih/',views.hadith_mainchapter, name='mishkat-al-masabih'),
    re_path(r'^mishkat-al-masabih/(?P<main_chp>\w+)/$', views.hadith_subchapter,name='hadith_subchapter'),
    # re_path(r'^mishkat-al-masabih/(?P<main_chp>\w+)/(?P<sr_no>\d+)/$', views.hadith_content,name='hadith_content'),
    re_path(r'^mishkat-al-masabih/(?P<main_chp>\w+)/(?P<sub_chp_id>\d+)/(?P<sr_no>\d+)/$', views.hadith_content,name='hadith_content'),

# <a href="{% url 'hadith_content' sub_chp=hadith.english_name sr_no=1 %}">test link </a>

    path('pdf_book_list',views.pdf_book_list, name='pdf_book_list'),



    # The Login page
    path('login', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
