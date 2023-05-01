from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    comments = models.TextField()

    def __str__(self):
        return self.email