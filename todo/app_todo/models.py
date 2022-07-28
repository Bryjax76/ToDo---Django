from datetime import datetime
from django.db import models
from django.forms import CharField, DateTimeField
from sqlalchemy import null

# Create your models here.

class List(models.Model):
    name = models.CharField(
        max_length=128,
        blank=True,
        null=False
    )
    description = models.CharField(
        max_length = 512,
        null=False
    )
    date = models.DateTimeField(
        default=datetime.now
    )
    
    def __str__(self):
        return self.name