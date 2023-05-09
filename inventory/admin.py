from django.contrib import admin
from .models import Device, Allocation, Team, TeamAllocation, DamagedDevice, Member, ResetPassword, Notification, DeviceType
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Device)
admin.site.register(Allocation)
admin.site.register(Team)
admin.site.register(TeamAllocation)
admin.site.register(DamagedDevice)
admin.site.register(Member)
admin.site.register(ResetPassword)
admin.site.register(Notification)
admin.site.register(DeviceType)