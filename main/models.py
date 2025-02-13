from django.db import models

class todo(models.Model):
    task = models.CharField(max_length=50)
