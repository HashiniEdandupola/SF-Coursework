from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    nic = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    nationality = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username