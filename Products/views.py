from django.shortcuts import render, redirect
from Products.models import Product, Review
from Products.forms import ProductsCreateForm, ReviewCreateForm
# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')



def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }


        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': reviews,
            'from': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    # if request.method == 'POST':
    #     product = Product.objects.get(id=product_id)
    #     reviews = Review.objects.filter(product=product)
    #
    #     form = ReviewCreateForm(data=request.POST)
    #     if form.is_valid():
    #         Review.objects.create(
    #             text=form.cleaned_data.get('text'),
    #             product=product
    #         )
    #         return redirect(f'/products/{product_id}')


        # return render(request, 'products/create.html', context={
        #         'product': product,
        #         'reviews': reviews,
        #         'form': form
        #     })


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductsCreateForm
        }
        return render(request, 'products/create.html', context=context)
#
    if request.method == 'POST':
        form = ProductsCreateForm(data=request.POST)

        if form.is_valid():
#             # print(form.cleaned_data.get('commentable')==False)
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                # commentable=form.cleaned_data.get('commentable')
            )
            return redirect('/products')
#
# #
        return render(request, 'products/create.html', context={
            'form': form
            })
#
#     if request.method == 'POST':
#         data = request.POST
#
#         """validation"""
#         errors = {}
#
#         if len(data['title']) < 1:
#             errors['title_errors'] = 'ploho'
#
#         if len(data['description']) < 1:
#             errors['description_errors'] = 'ploho'
#
#         if len(errors.keys()) < 1:
#             Product.objects.create(
#                 title=data['title'],
#                 description=data['description'],
#                 rate=data['rate']
#                     # commentable=form.cleaned_data.get('commentable')
#             )
#             return redirect('/Products/')
#
#         return render(request, 'products/create.html', context={'errors': errors})

