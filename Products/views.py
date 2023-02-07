from django.shortcuts import render, redirect
from Products.models import Product, Review
from Products.forms import ProductsCreateForm, ReviewCreateForm

PAGINATION_LIMIT = 1
# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')



def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        # print(request.GET.get('search'))
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = Product.objects.filter(
                description__icontains=search
            )  |  Product.objects.filter(
                title__icontains=search
            )
        """
        max page
        """
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        print(max_page)

        """
        slice products by stranica
        """
        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT*page]

        # max_page = products.__len__() / PAGINATION_LIMIT
        # if round(max_page) < max_page:
        #     max_page = round(max_page) + 1
        # else:
        #     max_page = round(max_page)
        #
        # print(max_page)

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page+1)
        }


        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)

        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author_id=request.user.id,
                text=form.cleaned_data.get('text'),
                product=product
            )
            return redirect(f'/products/{product_id}')


        return render(request, 'products/create.html', context={
                'product': product,
                'reviews': reviews,
                'form': form
            })


def create_product_view(request):
    if request.method == 'GET' and not request.user.is_anonymous:
        context = {
            'form': ProductsCreateForm
        }
        return render(request, 'products/create.html', context=context)

    elif request.user.is_anonymous:
        return redirect('/products')

    if request.method == 'POST':
        form = ProductsCreateForm(data=request.POST)

        if form.is_valid():
            print(form.cleaned_data.get('commentable')==False)
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                commentable=form.cleaned_data.get('commentable')
            )
            return redirect('/products')
#
# #
        return render(request, 'products/create.html', context={
            'form': form
            })
