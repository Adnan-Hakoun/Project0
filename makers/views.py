
 #==================function best view ===================================
#
# from django.shortcuts import render , redirect
# from .forms import Add_maker
# from .models import Maker
#
#
# def get_makers(request):
#     makers=Maker.objects.all()
#     return render(request,'makers.html',{'makers':makers})
#
#
# def add_maker(request):
#     if request.POST:
#         form=Add_maker(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/makers/')
#         else:
#             return redirect('/makers/add/')
#     empty_form=Add_maker()
#     return render(request,'add_maker.html',{'empty_form':empty_form})dd_product.html',{'empty_form':empty_form})
#
 #==================class best view ===================================
from django.views.generic import ListView , CreateView
from .models import Maker
from .forms import Add_maker

class GetMakers(ListView):
    queryset=Maker.objects.all()
    template_name='makers.html'

class AddMaker(CreateView):
    form_class=Add_maker
    template_name='add_maker.html'
    success_url='/makers/'































  #======================================================================
