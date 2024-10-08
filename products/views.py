from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductSearchForm


def home(request):
    return render(request, 'home.html')

def set_liked_by_user(products, user):
    if not isinstance(products, list):
            products = [products]

    for product in products:
        if user.is_authenticated:
            product.liked = user in product.liked_by.all()
        else:
            product.liked = False
    return products

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.kwargs.get('category', None)
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(context['object_list'])  # Convert QuerySet to list
        set_liked_by_user(products, self.request.user)
        context['object_list'] = products  # Update the context
        context['categories'] = Category.objects.all()  # To show categories as filters
        return context
    


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_liked_by_user([context['object']], self.request.user)

        return context

    


class LikeProductView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = Product.objects.get(id=product_id)

        if request.user in product.liked_by.all():
            product.liked_by.remove(request.user)
        else:
            product.liked_by.add(request.user)

        referer_url = request.META.get('HTTP_REFERER', reverse('product_list'))
        return_url = reverse('product_detail', args=[product_id])
        if return_url not in referer_url:
            return_url = reverse('product_list')

        return HttpResponseRedirect(return_url) 

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user in product.liked_by.all():
        product.liked_by.remove(request.user)
    else:
        product.liked_by.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@login_required
def favorite_products(request):
    products = request.user.liked_products.all()
    return render(request, 'favorite_products.html', {'products': products})
    
def search_products(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()
    
    context = {
        "form": form
    }
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            products = products.filter(name__icontains=query)
            
        context['object_list'] = products  # Update the context
        context['categories'] = Category.objects.all()
    return render(request, 'product_list.html', context)

