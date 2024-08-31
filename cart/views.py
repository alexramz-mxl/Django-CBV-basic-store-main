from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from products.models import Product
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render




class CartListView(ListView, LoginRequiredMixin):
    template_name = 'cart_detail.html'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        valid_cart_items = {}

        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(pk=product_id)
                valid_cart_items[product_id] = quantity
            except Product.DoesNotExist:
                continue
        request.session['cart'] = valid_cart_items
        
        cart_items = {Product.objects.get(pk=pid): qty for pid, qty in valid_cart_items.items()}

        total_price = sum(product.price * qty for product, qty in cart_items.items())
        
        return render(request, 'cart_detail.html', 
                      {'cart': cart_items,
                       'total_price': total_price
                       })

    def get_queryset(self):
        return self.request.session.get('cart', [])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_queryset()
        
        valid_products_ids = [pid for pid in cart if Product.objects.filter(id=pid).exists()]
        
        products_in_cart = Product.objects.filter(id__in=valid_products_ids)
        cart_items = {Product.objects.get(id=pid): cart[pid] for pid in valid_product_ids}
        
        context['cart_items'] = cart_items
        context['cart'] = cart
        context['total_price'] = sum(product.price * cart [product.id] for product in products_in_cart)
        
        return context
    
    
class ClearCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        request.session['cart'] = {}
        return HttpResponseRedirect(reverse('cart_detail'))
    


class AddToCartView(LoginRequiredMixin, CreateView):
    model = Product
    fields = []
    success_url = reverse_lazy('cart_detail')
    
    def post(self, request, *args, **kwargs):
        product_id = str(self.kwargs.get('pk'))
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        # If product is already in the cart, update quantity
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart
        return HttpResponseRedirect(reverse('cart_detail'))

    def form_valid(self, form):
        print('form_valid()')
        product_id = self.kwargs['pk']
        cart = self.request.session.get('cart', [])
        if product_id not in cart:
            cart.append(product_id)
        self.request.session['cart'] = cart
        return HttpResponseRedirect(self.get_success_url())


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, product_id, *args, **kwargs):
        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
        request.session['cart'] = cart
        return redirect(reverse('cart_detail'))

def payment_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            item_total = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
            total_price += item_total
        except Product.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'payment.html', context)