from django.shortcuts import render

from oriflamian_blog.ori_app.models import Product


def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'ori_app/store.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'ori_app/product_details.html', context)



