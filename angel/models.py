from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Angel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()

