 #==================function best view ===================================


# from django.shortcuts import render , redirect
# from .models import Product
# from .forms import Add_product
# from events.models import Event
#
#
# def get_products(request):
#     products=Product.objects.all()
#     return render(request,'products.html',{'products':products})
#
# def add_product(request):
#     if request.POST:
#         form=Add_product(request.POST)
#         if form.is_valid():
#             new_product=form.save()
#             new_event=Event.objects.create(type='add',product=new_product,source=request.user)
#             new_event.save()
#             return redirect('/products/')
#         else:
#             return redirect('/products/add/')
#
#
#     empty_form=Add_product()
#     return render(request,'add_product.html',{'empty_form':empty_form})
 #==================class best view ===================================
from django.views.generic import ListView , CreateView ,UpdateView
from .models import Product
from .forms import Add_product

class GetProducts(ListView):
    queryset = Product.objects.all()
    template_name='products.html'


class AddProducts(CreateView):
    form_class=Add_product
    template_name='add_product.html'
    success_url='/products/'   #this is instade of redirect

class UpdateProducts(UpdateView):
    form_class=Add_product
    template_name='add_product.html'
    success_url='/products/'





































#=====================================================================
