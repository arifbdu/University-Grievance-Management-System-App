from django.db import models

class Hostel(models.Model):
    name = models.TextField()
    student_id = models.IntegerField()
    session = models.IntegerField()
    room_no = models.IntegerField()
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
