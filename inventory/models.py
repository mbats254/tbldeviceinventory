from unittest.mock import DEFAULT
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Device(models.Model):      
    serial_number = models.CharField(max_length=70,unique=True)
    deviceTypeUniqid = models.CharField(max_length=70)    
    uniqid = models.CharField(max_length=35,  unique=True) 
    team_assigned_status = models.IntegerField(default=0)
    resource_assigned_status = models.IntegerField(default=0)
     
    def __str__(self):
        return f"{self.serial_number}"
    
class DeviceType(models.Model):
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=70)
    brand = models.CharField(max_length=70)
    poster_link = models.CharField(max_length=254)
    capacity = models.CharField(max_length=40, default=None, blank=True, null=True)
    storage_type = models.CharField(max_length=40, default=None, blank=True, null=True)
    RAM = models.CharField(max_length=40, default=None, blank=True, null=True)
    processor = models.CharField(max_length=40, default=None, blank=True, null=True)  
    uniqid = models.CharField(max_length=35, default=uuid.uuid4(), editable=False, unique=True) 
    
    def __str__(self):
        return f"{self.name}"

class Notification(models.Model):  
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    uniqid = models.CharField(max_length=35, editable=False, default=uuid.uuid4() ,unique=True) 
    link = models.CharField(max_length=70)
    status = models.IntegerField(default=0)
    user_uniqid = models.CharField(max_length=35)
    
    def __str__(self):
        return f"{self.title}"
    
    
class ResetPassword(models.Model):
    username = models.CharField(max_length=70)
    resetUniqid =  models.CharField(max_length = 35,  editable=False, unique=True, default=uuid.uuid4)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.resetUniqid}"
        
    
class Member(User):
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    rank = models.CharField(max_length=10, default="tester")
    full_name = models.CharField(max_length=70, default="tester")
    team = models.CharField(max_length=70, blank=True, null=True)
    status = models.IntegerField(default=0)
    user_photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
    def __str__(self):
        return f"{self.uniqid} {self.rank}"

class TokenStore(User):
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    access_token = models.CharField(max_length=70)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.uniqid}"
    
    
class Team(models.Model):
    name = models.CharField(max_length=70) 
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Allocation(models.Model):
    device_uniqid =  models.CharField(max_length=70)
    user_allocated = models.CharField(max_length=70)
    user_team = models.CharField(max_length=70, default=None, blank=True, null=True)
    use = models.CharField(max_length=70, default=None, blank=True, null=True)
    location = models.CharField(max_length=70)
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.uniqid}"

class TeamAllocation(models.Model):
    device_uniqid =  models.CharField(max_length=70)
    team_allocated = models.CharField(max_length=70)
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.uniqid}"

class DamagedDevice(models.Model):
    device_uniqid =  models.CharField(max_length=70)
    explained_issue = models.CharField(max_length=300)
    status = models.IntegerField(default=0)
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    complainant_team = models.CharField(max_length=70)
    user_uniqid = models.CharField(max_length=70)
    
    def __str__(self):
        return f"{self.uniqid}"
    
class Admin(models.Model):
    name =  models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class TeamLead(models.Model):
    name =  models.CharField(max_length=70)
    email = models.CharField(max_length=70, unique=True)
    user_uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    team = models.CharField(max_length=70)
    
    def __str__(self):
        return f"{self.name}"

class ReturnToOffice(models.Model):
    device_uniqid =  models.CharField(max_length=70)
    
    condition = models.CharField(max_length=70)
    user_uniqid = models.CharField(max_length=70)
    uniqid = models.CharField(max_length=35, default=uuid.uuid4, editable=False, unique=True)
    
    
    def __str__(self):
        return f"{self.name}"

    
    
        
    