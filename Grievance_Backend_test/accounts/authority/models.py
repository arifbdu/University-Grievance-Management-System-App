from django.db import models

class Authority(models.Model):

    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=15)
    batch = models.CharField(max_length=15)
    phone_no = models.IntegerField()
    data = models.TextField()
    importance = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High'), (5, 'Critical')])
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)