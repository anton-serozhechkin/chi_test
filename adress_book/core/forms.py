from django.forms import ModelForm
from django import forms
from .models import Record
from django_countries.fields import CountryField

class RecordFormChange(forms.Form):
    country = CountryField().formfield()

class RecordForm(ModelForm): 
    name = forms.CharField(label='Имя')
    city = forms.CharField(label='Город')
    street = forms.CharField(label='Улица')
    phone_number = forms.CharField(label='Телефонный номер')
    class Meta:
        model = Record
        fields = ['name', 
                  'country', 'city', 'street',
                  'phone_number']