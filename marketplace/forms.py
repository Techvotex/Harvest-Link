from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','location','image','quantity']
from django import forms
from .models import Product, Inquiry

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','location','image','quantity']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':3, 'placeholder':'Write message to farmer...'})
        }
