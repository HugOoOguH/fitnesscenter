from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
#View  list of products
def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category= category)
    return render (request, 'shop_product/product/product_list.html',
                    {'category': category,
                     'categories': categories,
                     'products': products})

#View detail od product
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id , slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop_product/product/product_detail.html', {'product': product,
                                                                'cart_product_form': cart_product_form})


