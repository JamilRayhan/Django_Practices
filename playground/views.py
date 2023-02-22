from operator import index
from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Musician,Album
from playground import forms
def home(request):
    diction= {'St':"I am Sample Text"}
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician', 'musician':musician_list}
    return render(request,'playground/index.html',context=diction)

def form(request): 
    new_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        
        if new_form.is_valid(): 
            new_form.save(commit=True)
            return home(request)
    diction={'test_form':new_form,'heading_1':"Add new Musician"}
    return render(request,'playground/form.html',context=diction)  