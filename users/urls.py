from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('card/<int:pk>/', views.membership_card_list, name='membership_card_list'),
    path('card/<int:pk>/', views.membership_card_detail, name='membership_card_detail'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
