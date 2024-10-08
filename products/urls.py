from django.urls import path
from .views import ProductListView, ProductDetailView, LikeProductView, home, search_products, toggle_favorite, favorite_products

urlpatterns = [
    path('home', home, name="home"),
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<str:category>/', ProductListView.as_view(), name='product_list_by_category'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('like/<int:product_id>/', LikeProductView.as_view(), name='like_product'),
    path('search/', search_products, name='search_products'),
    path('favorite/<int:product_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', favorite_products, name='favorite_products'),
]
