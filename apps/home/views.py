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

from .models import *
import requests





def quran_list_chapter(request):


    url = "https://api.quran.com/api/v4/chapters"
    payload = "{}"
    response = requests.request("GET", url, data=payload)

    json_response = response.json()
    chapter_list = json_response['chapters']
    context = {"chapter_list":chapter_list}

    html_template = loader.get_template('frontend/home.html')
    return HttpResponse(html_template.render(context, request))


def quran_get_chapter(request,chapter_id):

    url = "https://api.quran.com/api/v4/chapters/{id}?language=en".format(id=chapter_id)
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    json_response = response.json()
    chapter = json_response['chapter']

    quran_obj = QuranChapterOld.objects.filter(chapter_no=chapter_id).first()

    context = {"chapter":chapter,"quran":quran_obj}
    html_template = loader.get_template('frontend/quran_get_chapter.html')
    return HttpResponse(html_template.render(context, request))


def pdf_hadith_list(request):
    book_list = Book.objects.prefetch_related('bookpdf_set').all().filter(category='hadith')
    context = {"book_list":book_list}
    html_template = loader.get_template('frontend/pdf_book_list.html')
    return HttpResponse(html_template.render(context,request))

def pdf_dua_list(request):
    book_list = Book.objects.prefetch_related('bookpdf_set').all().filter(category='dua')
    context = {"book_list":book_list}
    html_template = loader.get_template('frontend/pdf_book_list.html')
    return HttpResponse(html_template.render(context,request))

def pdf_quran_list(request):
    book_list = Book.objects.prefetch_related('bookpdf_set').all().filter(category='quran')
    context = {"book_list":book_list}
    html_template = loader.get_template('frontend/pdf_book_list.html')
    return HttpResponse(html_template.render(context,request))


# mishkat-al-masabih/
def hadith_mainchapter(request):

    hadith_main_chapter_list = HadithBookMainChapter.objects.filter(hadithbook_id=1)
    print(hadith_main_chapter_list)
    context = {"hadith_main_chapter_list":hadith_main_chapter_list}
    html_template = loader.get_template('frontend/hadees_mainchapter.html')
    return HttpResponse(html_template.render(context,request))

# mishkat-al-masabih/faith/ XX
# mishkat-al-masabih/id/ 
def hadith_subchapter(request,main_chp):

    print("$$$ main_chp $$$", main_chp)
    obj = HadithBookMainChapter.objects.filter(english_name=main_chp).first()
    hadith_sub_chapter = HadithBookSubChapter.objects.filter(hadith_book_main_chapter_id=obj.id)

    context = {"hadith_sub_chapter":hadith_sub_chapter}
    html_template = loader.get_template('frontend/hadees_subchapter.html')
    return HttpResponse(html_template.render(context,request))

# mishkat-al-masabih/faith/
def hadith_content(request,main_chp,sub_chp_id,sr_no):
    try:
        print("share_hadith",main_chp)
        # main_chp = HadithBookMainChapter.objects.filter(english_name=main_chp).first()
        hadith_sub_chapter = HadithBookContent.objects.filter(hadith_book_sub_chapter_id=sub_chp_id,sr_no=sr_no).first()
        print("sub_chapter_name",hadith_sub_chapter.hadith_book_sub_chapter)
        context = {"isfound":True,"content":hadith_sub_chapter,"hadith_book_main_chapter":main_chp,"sub_chapter_name":hadith_sub_chapter.hadith_book_sub_chapter.sub_chapter_name}
        html_template = loader.get_template('frontend/hadith_single_content.html')
        return HttpResponse(html_template.render(context,request))
    except:

        context = {"isfound":False}
        html_template = loader.get_template('frontend/hadith_single_content.html')
        return HttpResponse(html_template.render(context,request))

def t_hadith_content(request,main_chp,id_no):
    print("****sr_no",id_no,main_chp)
    try:
        print("share_hadith",main_chp)
        # main_chp = HadithBookMainChapter.objects.filter(english_name=main_chp).first()
        hadith_sub_chapter = HadithBookContent.objects.filter(id=id_no).first()
        print("sub_chapter_name",hadith_sub_chapter.hadith_book_sub_chapter)
        context = {"isfound":True,"content":hadith_sub_chapter,"hadith_book_main_chapter":main_chp,"sub_chapter_name":hadith_sub_chapter.hadith_book_sub_chapter.sub_chapter_name}
        html_template = loader.get_template('frontend/hadith_single_content.html')
        return HttpResponse(html_template.render(context,request))
    except:

        context = {"isfound":False}
        html_template = loader.get_template('frontend/hadith_single_content.html')
        return HttpResponse(html_template.render(context,request))



def hadith_book_excel_file(request):
    context = {"isfound":False}
    html_template = loader.get_template('frontend/hadith_single_content.html')
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


