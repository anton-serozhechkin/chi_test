from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm, RecordFormChange
from django.db.models import Q

def home(request):
    record_list = Record.objects.filter(is_active=True).order_by('-created')
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
    return render(request, 'records/records_list.html', locals())

def record_detail(request, record_id):
    data_record = get_object_or_404(Record, id=record_id)
    return render(request, 'records/record_detail.html', locals())

def delete_record(request, record_id):
    Record.objects.filter(id=record_id).delete()
    return redirect('home')

def search_results(request):
    if request.GET.get('q'):
        query = request.GET.get('q')

        results = Record.objects.filter(
            Q(name__icontains=query)|
            Q(country__icontains=query)|
            Q(city__icontains=query)|
            Q(street__icontains=query)|
            Q(phone_number__icontains=query)
        ).order_by('-created')

    else:    
        empty_req = 'Пустой запрос'

    return render(request, 'records/search.html', locals())

def change_record(request, record_id):
    data_record = get_object_or_404(Record, id=record_id)
    if request.method == "POST":
        form = RecordFormChange(request.POST)
        if request.POST['name']:
            if request.POST['name'] != data_record.name:
                data_record.name = request.POST['name']
                data_record.save()                 
        
        if form.is_valid():
            data_record.country = request.POST['country']
            data_record.save()
                       
        if request.POST['city']:
            if request.POST['city'] != data_record.city:
                data_record.city = request.POST['city']
                data_record.save() 
        
        if request.POST['street']:
            if request.POST['street'] != data_record.street:
                data_record.street = request.POST['street']
                data_record.save()
        if request.POST['phone_number']:
            if request.POST['phone_number'] != data_record.phone_number:
                data_record.phone_number = request.POST['phone_number']
                data_record.save()
        return redirect('home')
    else:
        form = RecordFormChange()
    return render(request, 'records/change_record.html', locals())
