from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from.models import Order
# Create your views here.

@login_required(login_url='loginview_url')
def addOrderView(request):
    form = OrderForm()
    template_name = "app1/add.html"
    context = {'form': form}
    if request.method == 'POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

@login_required(login_url='loginview_url')
def showOrderView(request):
    data = Order.objects.all()
    template_name = 'app1/show.html'
    context = {'obj':data}
    return render(request, template_name, context)



def updateOrderView(request, pk):
    #print("value of pk:", pk)
    ord = Order.objects.get(id = pk)
    #print(ord)
    form = OrderForm(instance=ord)
    template_name = 'app1/add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=ord)
        if form.is_valid():
            form.save()
            return redirect('showorder_url')
    return render(request, template_name, context)


def deleteOrderView(request, pk):
    ord = Order.objects.get(id=pk)
    template_name = 'app1/confirm.html'
    context = {'data':ord}
    if request.method=="POST":

        ord.delete()
        #print(ord)
        return redirect('showorder_url')
    return render(request,template_name, context)