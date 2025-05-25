from django.db import models

class CPIForecast(models.Model):
    date = models.DateField(unique=True)
    actual_cpi = models.FloatField(null=True, blank=True)
    predicted_cpi = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}: {self.predicted_cpi}"
