from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from accounts.models import Administrator


def order_create(request):
    cart = Cart(request)
    administrator =  get_object_or_404(Administrator, user_administrator=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order = order,
                                         product = item['product'],
                                         price = item['price'],
                                         quantity=item['quantity'])
            #Clear the cart
            cart.clear()
            return render (request, 'orders/order/created.html',{'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',{'cart':cart, 'form': form})
