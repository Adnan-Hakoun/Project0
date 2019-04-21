from django.shortcuts import render , redirect
from .forms import Add_maker
from .models import Maker


def get_makers(request):
    makers=Maker.objects.all()
    return render(request,'makers.html',{'makers':makers})


def add_maker(request):
    if request.POST:
        form=Add_maker(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/makers/')
        else:
            return redirect('/makers/add/')
    empty_form=Add_maker()
    return render(request,'add_maker.html',{'empty_form':empty_form})
