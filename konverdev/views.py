from django.shortcuts import render
from .queries import *

def products(request):
    try:
        products = GetProducts();
        tags = GetTags();
        if 'remove' in request.POST:
            DeleteProduct(request.POST['remove'])
        if 'save' in request.POST:
            UpdateProduct(request.POST['id'], request.POST['title'], request.POST['tag'], request.POST['img_path'], request.POST['price'], request.POST['unit'])
        if 'add' in request.POST:
            InsertProduct(request.POST['title'], request.POST['tag'], request.POST['img_path'], request.POST['price'], request.POST['unit'])
    finally:
        pass
    return render(request, 'product.html', locals())

def product_edit(request):
    try:
        product = GetProduct(request.POST['edit'])[0]
        tags = GetTags()
    finally:
        pass
    return render(request, 'product_edit.html', locals())

def wagon(request):
    try:
        wagon_id = None
        if 'add' in request.POST:
            wagon_id = request.POST['wagon']
            ChangeCountProductToWagon(request.POST['wagon'], request.POST['add'], 1)
        if 'sub' in request.POST:
            wagon_id = request.POST['wagon']
            ChangeCountProductToWagon(request.POST['wagon'], request.POST['sub'], -1)
        if 'insert' in request.POST:
            wagon_id = request.POST['insert']
            UpdateStock(request.POST['insert'], request.POST['product'], request.POST['count'])
        if 'clear' in request.POST:
            wagon_id = request.POST['clear']
            ClearWagon(request.POST['clear'])
        if 'goto' in request.POST:
            wagon_id = request.POST['goto']
        products = GetProducts()
        wagons = GetWagons();
        if (wagon_id == None):
            wagon_id = wagons[0].id
        wagon = GetWagon(wagon_id)
    finally:
        pass
    return render(request, 'wagon.html', locals())