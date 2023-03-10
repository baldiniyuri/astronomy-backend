from django.db import models


class Defense(models.Model):
    ip = models.CharField(max_length=255)
    attack_date = models.DateTimeField(auto_now_add=True, blank=True) 
    route = models.CharField(max_length=255)