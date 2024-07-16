from django.shortcuts import render
from afisha import Movie

def product_view(request):
    return render(request, template_name='index.html')

def main_page_view(request):
    products = Movie.objects.all()
    print(products)
    context = {
        'product_list': products
    }
    return render(request, template_name='index.html', context=context)