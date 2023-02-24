from operator import index
from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Musician,Album
from playground import forms

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {"title":"Home Page",'musician_list':musician_list}
    return render(request,'playground/index.html',context=diction)


def album_list(request):
    diction={'title':"List of Albums"}
    return render(request,'playground/album_list.html',context=diction)

def musician_form(request):
    form=forms.MusicianForm()
    
    if request.method=="POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    diction = {'title':"Add Musician",'musician_form':form}
    return render(request,'playground/musician_form.html',context=diction)

def album_form(request):
    form = forms.AlbumForm()
    
    if request.method=="POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':"Add Album",'album_form':form}
    return render(request,'playground/album_form.html',context=diction)
