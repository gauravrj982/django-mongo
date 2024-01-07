from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateItem
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, 'todo/index.html', {'item_list': item_list})

def addItem(request):
    create = CreateItem()
    if request.method == 'POST':
        create = CreateItem(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('index')
        else:
            return HttpResponse('Some Error occured')
    else:
        return render(request, 'todo/add_item.html', {'item_list':create})
