from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phoneNumber = models.CharField(max_length=255, unique=True)
    language = models.CharField(max_length=100)
    currency = models.CharField(max_length=4)
    createdAt = models.DateTimeField(auto_now_add=True)





