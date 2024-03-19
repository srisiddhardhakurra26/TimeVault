from django.db import models
from django.contrib.auth.models import User

class TimeCapsule(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    open_date = models.DateField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)