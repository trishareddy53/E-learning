from django.db import models

# Create your models here.

class User(models.Model):
    regdno = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# user = User(regdno='20331A1220', password='webcap')
# user.save()
