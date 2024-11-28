
from django.db import models

class Feedback(models.Model):
    name = models.TextField()
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

