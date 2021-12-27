from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class client(models.Model):
    client_name=models.CharField('client name', max_length=120)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=120)

    def __str__(self):
        return self.client_name

class project(models.Model):
    project_name=models.CharField('project_name', max_length=120)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=120)
    client=models.ForeignKey(client, on_delete=models.CASCADE ,related_name ='projects', null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name