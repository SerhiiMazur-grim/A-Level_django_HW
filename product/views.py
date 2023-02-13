from django.shortcuts import render

def prod_list(request):
    return render(request, 'product/store.html')

def product(request):
    return render(request, 'product/product.html')
