from django import forms



class ProductSearchForm(forms.Form):
    query = forms.CharField(
        label='Search for product',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search for product'})   
    )