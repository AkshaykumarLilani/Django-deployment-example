from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
