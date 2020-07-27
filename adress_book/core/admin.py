from django.contrib import admin
from .models import *


class RecordAdmin(admin.ModelAdmin):
    list_filter = ('is_active', )
    search_fields = ('name', 'country__name', 'city', 'street', 'phone_number')
    fieldsets = (
        ('Основная информация', {
            'fields':(
                'name',
                'country',
                'city',
                'street',
                'image',
                'phone_number'
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('created', 'is_active')
            }
            )
    )

admin.site.register(Record, RecordAdmin)
