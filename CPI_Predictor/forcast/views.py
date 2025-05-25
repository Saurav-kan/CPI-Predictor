from rest_framework import viewsets
from django.shortcuts import render
from .models import CPIForecast
from .serializers import CPIForecastSerializer
from .services import run_cpi_forecast

class CPIForecastViewSet(viewsets.ModelViewSet):
    queryset = CPIForecast.objects.order_by('-date')
    serializer_class = CPIForecastSerializer

def index(request):
    # Defaults values
    start_year = 2015
    end_year   = 2024
    horizon    = 1
    forecast_results = None

    if request.method == "POST":
        start_year = int(request.POST.get("start_year", start_year))
        end_year   = int(request.POST.get("end_year",   end_year))
        horizon    = int(request.POST.get("horizon",    horizon))

        forecast_results = run_cpi_forecast(start_year, end_year, horizon)

        for f_date, pred in forecast_results:
            CPIForecast.objects.update_or_create(
                date=f_date,
                defaults={"predicted_cpi": pred}
            )

    return render(request, "forcast/index.html", {
        "forecast_results": forecast_results,
        "start_year":       start_year,
        "end_year":         end_year,
        "horizon":          horizon,
    })
