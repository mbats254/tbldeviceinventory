from rest_framework import serializers
from .models import Device, Notification,Admin, Allocation, Team, TeamAllocation, TeamLead, DamagedDevice, User, DeviceType ,Member, ResetPassword, ReturnToOffice



        
class ReturnToOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnToOffice
        fields = '__all__'
        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        
class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamAllocation
        fields = '__all__'

class TeamLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLead
        fields = '__all__'

class DamagedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamagedDevice
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class ReturnToOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnToOffice
        fields = '__all__'        