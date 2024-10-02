from django.db import models

class datas(models.Model):
    
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=120)