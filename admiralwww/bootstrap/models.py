from django.db import models

# Create your models here.

class Params(models.Model):
    key = models.CharField(max_length=50, db_index=True)    
    value = models.TextField()
    hint = models.CharField(max_length=255)