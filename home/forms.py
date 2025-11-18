from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']



class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email Address'}))
