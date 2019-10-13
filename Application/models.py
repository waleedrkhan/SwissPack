from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    photo = models.FileField(upload_to='images/', null=True, verbose_name="")


class Users(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10, default="l_name")
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_id = models.CharField(max_length=25)
    about_me = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=50, default="")

