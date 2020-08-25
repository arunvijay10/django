from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.
def index(request):
    # return HttpResponse("Hello");
    products=product.object.all()
    return render(request,'index.html',{"products":products})
def contact(request):
    return HttpResponse("contact")