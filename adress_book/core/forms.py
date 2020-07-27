from django.forms import ModelForm
from django import forms
from .models import Record
from django_countries.fields import CountryField


class RecordForm(ModelForm): 
    
    country = CountryField().formfield(label='Страна', required=False)
    name = forms.CharField(label='Имя')
    city = forms.CharField(label='Город', required=False)
    street = forms.CharField(label='Улица', required=False)
    phone_number = forms.CharField(label='Телефонный номер')
    image = forms.ImageField(label='Фотография', required=False)
    
    class Meta:
        model = Record
        fields = ['name', 'country',
                  'city', 'street',
                  'phone_number', 'image']