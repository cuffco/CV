from django.forms import ModelForm
from django import forms
from django.forms.utils import ErrorList

from .models import Contact


class ContactForm(ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Prénom', 'size': 30}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nom', 'size': 30}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Téléphone', 'size': 30}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'size': 30}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Message", 'rows': 4, 'cols': 40, }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'message']


# Manage Error in account page
class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div style="color: white;" class="errorlist">%s</div>' % ''.join(
            ['<p class="small error">%s</p>' % e for e in self])
