from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, MembershipCard

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']
        
class MembershipCardForm(forms.ModelForm):
    class Meta:
        model = MembershipCard
        fields = ['first_name', 'last_name', 'membership_number', 'profile_photo', 'membership_type', 'benefits']
        
class ContactForm(forms.Form):
    email = forms.EmailField(label='Your email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        label='Category',
        choices=[('general', 'General Inquiry'),('support', 'Support'), ('feedback', 'Feedback')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(label='Additional details', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    