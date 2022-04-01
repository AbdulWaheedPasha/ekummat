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


def home(request):
    context = {}
    html_template = loader.get_template('frontend/home.html')
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
