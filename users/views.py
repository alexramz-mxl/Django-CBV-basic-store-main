from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, ProfilePictureForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from .models import MembershipCard

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('product_list')

class CustomLogoutView(LogoutView):
    next_page = '/'

def membership_card_list(request):
    cards = MembershipCard.objects.all()
    return render(request, 'membership_card_list.html', {'cards': cards})

def membership_card_detail(request, pk):
    card = get_object_or_404(MembershipCard, pk=pk)
    return render(request, 'membership_card_detail', {'card': card})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['details'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.CONTACT_EMAIL],
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
