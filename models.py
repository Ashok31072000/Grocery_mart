from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    psw = models.CharField(max_length=30)
    phonenum = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    h_no = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class query(models.Model):
    query = models.CharField(max_length=300)