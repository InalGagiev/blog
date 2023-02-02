from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=50)
    anons = models.CharField(max_length=250)
    full_text = models.TextField(blank='True')
