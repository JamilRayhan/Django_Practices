from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    diction = {'text_1':'I am from views.py'}
    return render(request,'playground/index.html',context=diction)
