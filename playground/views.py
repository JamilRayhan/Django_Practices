from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Musician,Album
from playground import forms
def home(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician', 'musician':musician_list}
    return render(request,'playground/index.html',context=diction)

def form(request): 
    new_form = forms.user_form()
    diction = {'test_form':new_form,'heading_1':'this is from Dango Library'}
    
    if request.method=='POST':
        new_form=forms.user_form(request.POST)
        diction.update({'test_form':new_form})
        if new_form.is_valid():
            field=new_form.cleaned_data['field']
         
            diction.update({'field':field})
            diction.update({'form_s':"Yes"})
    
    return render(request,'playground/form.html',context=diction)