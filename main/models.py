import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
     
class project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class employeed(models.Model):
    departement = models.CharField(max_length=180)
    project  = models.ManyToManyField(project)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

