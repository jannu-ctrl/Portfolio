from django.db import models

# Create your models here.
class Job (models.Model): #MODEL CLS
    image=models.ImageField(upload_to='image/')
    summary=models.CharField(max_length=150)
    description=models.CharField(max_length=1000)