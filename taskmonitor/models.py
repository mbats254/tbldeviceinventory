from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now

# Create your models here.
class Task(models.Model):  
   
    taskName = models.CharField(max_length=70)
    taskType = models.CharField(max_length=70)
    
    uniqid = models.UUIDField(editable=False, default=uuid.uuid4() ,unique=True) 
    status = models.IntegerField(default=0)
   
       
    
    def __str__(self):
        return f"{self.jobName}"
    
    
class TaskMonitor(User):
    taskuniqid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    resourceUniqid = models.CharField(max_length=70)
    status = models.CharField(default="not started", max_length=255)
    endTime = models.DateTimeField(default=None,  null=True, blank=True)
    def __str__(self):
        return f"{self.uniqid} {self.rank}"  