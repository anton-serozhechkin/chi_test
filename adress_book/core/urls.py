from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', AcmeBookList.as_view(), name='home')
]