from django.shortcuts import render, redirect
from Shop.models import Order
from .forms import OrderForm
# Create your views here.
def Home(request):
    return render(request , "index.html")

def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'success.html')
        else:
            print(form.errors)
            return render(request, 'failed.html')
    else:
        form = OrderForm() 
    return render(request, 'failed.html')
    




