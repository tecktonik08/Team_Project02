import sqlite3
import mpld3
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    path = request.path
    resultstr = ''
    if path == 'index':
        resultstr = '<h1>TEAM 1</h1>'
    else :
        resultstr = '<h1>SemiProject</h1>'
    return HttpResponse(resultstr)


def home(request):
    result = {'first':'SemiProject', 'second':'TEAM 1'}
    return render(request, 'home.html', context=result)


def news(request):
    result = dict()
    db_news = sqlite3.connect('static/news.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 키워드
    keyword = request.GET.get('keyword')
    result['keyword'] = keyword

    # 키워드를 다룬 뉴스기사들
    c.execute("select id, date,press,title,topkeyword,url from newspapers where topkeyword like '%{}%';".format(keyword))
    data = c.fetchall()
    result['erows'] = data


    # 개수
    c.execute("select count(*) from newspapers where topkeyword like '%{}%';".format(keyword))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    # 모달창





    return render(request, 'news.html', result)



def analysis(request):
    return render(request, 'analysis.html')




def sample(request):
    return render(request, 'sample.html')
