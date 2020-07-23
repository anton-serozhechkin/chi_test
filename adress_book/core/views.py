from django.shortcuts import render
from .models import Record
from django.views.generic import ListView

class AcmeBookList(ListView):

    context_object_name = 'record_list'
    queryset = Record.objects.filter(is_active=True).order_by('-created')
    template_name = 'records/records_list.html'
    