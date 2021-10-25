from django.shortcuts import render
from .models import  Product
# Create your views here.
from django.core.paginator import Paginator


def index(request):
    product=Product.objects.all()
    #search code
    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        product=product.filter(title__icontains=item_name)

    #paginator code
    paginator=Paginator(product,4)
    page =request.GET.get('page')
    product=paginator.get_page(page)
    return  render(request,'index.html',{'products':product})


def detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'detail.html',{'product':product})

