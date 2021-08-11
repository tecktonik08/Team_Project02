from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

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

def info(request):
    return render(request, 'info.html')

def analysis(request):
    return render(request, 'analysis.html')
