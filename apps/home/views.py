# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Book,BookPDF
import requests

def quran_list_chapter(request):


    url = "https://api.quran.com/api/v4/chapters"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    print(response.text)
    # import json
    # chapter_list = json.loads(response)
    json_response = response.json()
    chapter_list = json_response['chapters']
    context = {"chapter_list":chapter_list}

    html_template = loader.get_template('frontend/home.html')
    return HttpResponse(html_template.render(context, request))


def quran_get_chapter(request,chapter_id):
    print("quran_get_chapter")
    print(chapter_id)
    url = "https://api.quran.com/api/v4/verses/by_chapter/1"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    print(response.text)
    json_response = response.json()
    chapter_list = json_response
    context = {"chapter_list":chapter_list}
    html_template = loader.get_template('frontend/quran_get_chapter.html')
    return HttpResponse(html_template.render(context, request))


def pdf_book_list(request):
    book_list = Book.objects.prefetch_related('bookpdf_set').all()
    # books = Book.objects.all()
    # bookpdf = BookPDF.objects.all()
    context = {"book_list":book_list}
    html_template = loader.get_template('frontend/pdf_book_list.html')
    return HttpResponse(html_template.render(context,request))

def hadees_mainchapter(request):
    context = {}
    html_template = loader.get_template('frontend/hadees_mainchapter.html')
    return HttpResponse(html_template.render(context,request))

def hadees_subchapter(request):
    context = {}
    html_template = loader.get_template('frontend/hadees_subchapter.html')
    return HttpResponse(html_template.render(context,request))



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
