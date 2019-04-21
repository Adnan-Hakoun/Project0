from django.shortcuts import render , redirect
from .models import Product
from .forms import Add_product
from events.models import Event


def get_products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def add_product(request):
    if request.POST:
        form=Add_product(request.POST)
        if form.is_valid():
            new_product=form.save()
            new_event=Event.objects.create(type='add',product=new_product,source=request.user)
            new_event.save()
            return redirect('/products/')
        else:
            return redirect('/products/add/')


    empty_form=Add_product()
    return render(request,'add_product.html',{'empty_form':empty_form})
