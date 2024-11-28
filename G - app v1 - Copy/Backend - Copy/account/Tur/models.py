from django.db import models

class TurbidityData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust max_digits and decimal_places as needed

    #def __str__(self):
        #return f'pH: {self.value} at {self.timestamp}'
