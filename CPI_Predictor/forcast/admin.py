from django.contrib import admin
from .models import CPIForecast

@admin.register(CPIForecast)
class CPIForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'predicted_cpi', 'actual_cpi')
    list_filter  = ('date',)
    ordering     = ('-date',)
