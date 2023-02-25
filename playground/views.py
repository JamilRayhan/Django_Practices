from operator import index
from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Musician,Album
from playground import forms
from django.db.models import Avg

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {"title":"Home Page",'musician_list':musician_list}
    return render(request,'playground/index.html',context=diction)


def album_list(request,id):
    artist_info = Musician.objects.get(pk=id)
    album_list = Album.objects.filter(artist=id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=id).aggregate(Avg('num_stars'))
    
    diction={'title':"List of Albums",'artist_info':artist_info,'album_list':album_list,'artist_rating':artist_rating}
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

def edit_artist(request, id):
    artist_info = Musician.objects.get(pk=id)
    form=forms.MusicianForm(instance=artist_info)
    diction ={'edit_form':form}
    return render(request,'playground/edit_artist.html',context=diction)