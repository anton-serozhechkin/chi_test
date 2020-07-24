from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('<int:record_id>/', record_detail, name='record_detail'),
    path('<int:record_id>/delete_record', delete_record, name='delete_record'),
    path('<int:record_id>/change_record', change_record, name='change_record'),
    path('search/', search_results, name='search_results'),

]