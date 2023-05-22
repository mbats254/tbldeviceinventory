from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes ,renderer_classes
from rest_framework.response import Response
from .serializers import DeviceSerializer,  AdminSerializer, MemberSerializer, ResetPasswordSerializer , DeviceTypeSerializer , AllocationSerializer,  TeamSerializer, DamagedDeviceSerializer, TeamAllocationSerializer,  TeamLeadSerializer
from auth.serializers import MyTokenObtainPairSerializer
from .models import Device, Admin, Allocation, Team, TeamAllocation, TeamLead, DamagedDevice, Member, ResetPassword, DeviceType
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, JSONParser, FileUploadParser
from django.http import JsonResponse
import uuid
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
import pandas as pd
from django.template.loader import render_to_string
# import uuid
from django.conf import settings
import random
import openpyxl
from django.core.files.storage import FileSystemStorage
import re
import json
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'user_routes-GET':'/inventory/user',
        'admin_routes-GET' :'/inventory/admin',
        'lead_routes-GET':'/inventory/lead',            

    }
    return Response(api_urls)


@api_view(['GET'])
def userApiOverview(request):
    api_urls = {
        'my_devices--GET':'/inventory/user/my/devices/<str:uniqid>',
        'single_device-GET' :'/inventory/user/single/device/<str:uniqid>/',
        'add_my_allocated_device-POST':'/inventory/user/add/my/device/',
        'report_damaged_device-POST':'/inventory/user/report/damaged/device/',       

    }
    return Response(api_urls)

@api_view(['GET'])
def leadApiOverview(request):
    api_urls = {
        'my_devices-GET':'/inventory/lead/my/devices/<str:uniqid>',
        'single_device-GET' :'/inventory/lead/device/<str:uniqid>/',
        'all_team_member_devices-POST':'/inventory/lead/all/team/user/devices/',
        'team_shared_devices-GET':'/inventory/lead/team/shared/devices/',
        'view_damaged_devices-GET':'/inventory/lead/view/damaged/devices/',
        'add_team_shared_devices-POST' :'/inventory/lead/add//team/shared/device/',
        'assign_new_device-POST' :'/inventory/lead/assign/new/device/',
        'all_team_members-GET' :'/inventory/lead/all/team/members/',
        'single_team_member-GET' :'/inventory/lead/single/team/member/<str:uniqid>'
       

    }
    return Response(api_urls)

@api_view(['GET'])
def adminApiOverview(request):
    api_urls = {
        'add_new_device-POST' :'/inventory/admin/add/new/device/',
        'single_device-GET' :'/inventory/admin/single/device/<str:uniqid>/',
        'all_user_devices-GET':'/inventory/admin/all/user/devices/',
        'all_teams-GET' :'/inventory/admin/all/teams/',
        'single_team-GET':'/inventory/admin/single/team/<str:uniqid>/',
        'all_team_shared_devices-GET':'/inventory/admin/all/team/shared/devices/',
        'view_damaged_devices-GET':'/inventory/admin/view/damaged/devices/',
        'all_users-GET':'/inventory/admin/all/users/',
        'admin_add_lead-POST':'/inventory/admin/add/team/lead/',
        'admin_all_leads-GET':'/inventory/admin/aadmin/all/leads/',
       

    }
    return Response(api_urls)

@api_view(['POST'])
def getUser(request): 
    # return Response((request.data['username']))      
    # if Member.objects.get(username = request.data['username']).exists():
    # try:
        user = Member.objects.get(username = request.data['username'])
        serializer =  MemberSerializer(user, many=False)
        return Response(serializer.data)
    # except Member.DoesNotExist:
    #     user = Member.objects.get(username = request.data['username'])
    #     serializer = UserSerializer(user, many=False)
    #     return Response(serializer.data)

@api_view(['POST'])
def userForgetPassword(request): 
    # return Response((request.data['username']))      
    # if Member.objects.get(username = request.data['username']).exists():
        user = Member.objects.get(username = request.data['username'])
        serializer =  MemberSerializer(user, many=False)
        daita = {"username" : request.data['username'], "resetUniqid": uuid.uuid4()}
        resetSerializer = ResetPasswordSerializer(data=daita)
        if resetSerializer.is_valid():
            # serializer.uniqid = uuid.uuid4()
            resetSerializer.save()
            # return Response(resetSerializer.data['resetUniqid'])
            resetPasswordLink = 'http://localhost:3000/reset/password/:'+str(resetSerializer.data['resetUniqid'])
            message = 'Hello '+serializer.data['username']+',\n \n Your password Reset link is \n \n'+resetPasswordLink
            send_mail('Forgot Password',message,settings.EMAIL_HOST_USER,[serializer.data['email']])
            return Response(resetSerializer.data)
        return Response(resetSerializer.errors)
        

@api_view(['POST'])
def resetPasswordview(request):    
    resetPassword = ResetPassword.objects.get(resetUniqid = request.data['resetUniqid'])
    resetPasswordSerializer = ResetPasswordSerializer(resetPassword, many=False)
    return Response(resetPasswordSerializer.data)

@api_view(['POST'])
def resetPasswordPost(request):
    user = Member.objects.get(username = request.data['username'])
    # password = set_password(request.data['password'])       
    user.set_password(request.data['password'])
    user.save()

    # return Response()  
       
    resetPassword = ResetPassword.objects.get(resetUniqid = request.data['resetUniqid'])
    daita = {"status": 1}
    resetPasswordSerializer = ResetPasswordSerializer(resetPassword, data=daita, partial=True)
    if resetPasswordSerializer.is_valid():
        # serializer.uniqid = uuid.uuid4()
        resetPasswordSerializer.save()
    return Response(resetPasswordSerializer.data)
      
    
    
    

@api_view(['POST'])
def readExcel(request): 
    # return Response((request.data['username']))   
        # print(request.FILES.get('excel_file'))
        excel_file = request.FILES.get("excel_file")
        # print(excel_file)
        df = pd.read_excel(excel_file)
        # print(df)
        # return Response(df)
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb['Data']
        return Response(worksheet)

        # excel_data = list()
        # # iterating over the rows and
        # # getting value from each cell in row
        # for row in worksheet.iter_rows():
        #     row_data = list()
        #     for cell in row:
        #         row_data.append(str(cell.value))
        #     excel_data.append(row_data)

        # return render(request, 'myapp/index.html', {"excel_data":excel_data}) 

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser,FileUploadParser])
def userUpdateProfile(request): 
    # return Response(request.data) 
    # daita = {request.data}  z
    # return Response(request.data['user_photo']) 
    # return Response(request.data)
    user = Member.objects.get(username = request.data['username'])
    # serializer =  MemberSerializer(user, many=False)
    second_serializer = MemberSerializer(user, data=request.data, partial=True) 
    # return Response(second_serializer.data) 
    if second_serializer.is_valid():
        # serializer.uniqid = uuid.uuid4()
        second_serializer.save()
    return Response(second_serializer.data) 

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser,FileUploadParser])
def leadReturnDeviceOffice(request): 
    return Response(request.data) 
    # daita = {request.data}  z
    # return Response(request.data['user_photo']) 
    # return Response(request.data)
    user = Member.objects.get(username = request.data['username'])
    # serializer =  MemberSerializer(user, many=False)
    second_serializer = MemberSerializer(user, data=request.data, partial=True) 
    # return Response(second_serializer.data) 
    if second_serializer.is_valid():
        # serializer.uniqid = uuid.uuid4()
        second_serializer.save()
    return Response(second_serializer.data) 
  


@api_view(['POST'])
def userSearchDevice(request):
    # return Response(request.data['userUniqid'])
    user = Member.objects.get(uniqid = request.data['userUniqid'])
    userSerializer = MemberSerializer(user, many=False)
    # return Response(userSerializer.data)    
    userAllocation = Allocation.objects.filter(user_allocated = userSerializer.data['uniqid'])
    userAllocationSerializer = AllocationSerializer(userAllocation, many=True)
    # return Response(userAllocationSerializer.data)
    foundArray = []
    for allocation in userAllocationSerializer.data:
        return Response(allocation['device_uniqid'])
        deviceDetails = Device.objects.get(uniqid = allocation['device_uniqid'])
        deviceSerializer = DeviceSerializer(deviceDetails, many=False)
        deviceType = DeviceType.objects.get(uniqid = deviceSerializer.data['deviceTypeUniqid']) & DeviceType.objects.filter(name__contains = request.data['search_item']) | DeviceType.objects.filter(brand__contains = request.data['search_item']) 
        foundArray.append(deviceType)
        if len(foundArray) > 0:
            return Response(foundArray)
        else:
            return Response('No Results found')

@api_view(['POST'])
def adminSingleUserDevices(request):    
    devices = Allocation.objects.filter(user_allocated = request.data['uniqid'])
    serializer =  AllocationSerializer(devices, many=True)
    i = 0
    allDevices = []
    allAllocation = []
    allAllocation.append(serializer.data)
    data_to_be_displayed = dict()
    data_to_be_displayed['allocation'] = serializer.data
    while i<len(serializer.data):
            # return Response(assignedPlatformsSerializer.data[i])
            deviceDetails = Device.objects.get(uniqid = serializer.data[i]['device_uniqid'])
            deviceSerializer  = DeviceSerializer(deviceDetails, many=False)            
            allDevices.append(deviceSerializer.data)           
            i = i + 1 
    data_to_be_displayed['allDevices'] = allDevices
    return Response(allDevices) 

@api_view(['POST'])
def adminSingleDeviceAllocation(request): 
    # return Response(request.data)   
    allAllocation = {}
    deviceDetail = Device.objects.get(uniqid = request.data['device_uniqid'])
    detailSerializer = DeviceSerializer(deviceDetail, many=False)
   
    try:
        teamDevice = TeamAllocation.objects.get(device_uniqid = request.data['device_uniqid'], status=1)       
        teamAllocationSerializer = TeamAllocationSerializer(teamDevice, many=False)
        allAllocation['teamAllocation'] = teamAllocationSerializer.data
        allAllocation['teamAllocation']['deviceSerialNumber'] = detailSerializer.data['serial_number']
        try:
            device = Allocation.objects.get(device_uniqid = request.data['device_uniqid'], status=1)
            resourceAllocationSerializer = AllocationSerializer(device, many=False)
            allAllocation['resourceAllocation'] = resourceAllocationSerializer.data        
            return Response(allAllocation)
        except Allocation.DoesNotExist:
            allAllocation['resourceAllocation'] = "Resource Allocation Does Not Exist||"+request.data['device_uniqid']+"||"+detailSerializer.data['serial_number']          
        return Response(allAllocation)
    except TeamAllocation.DoesNotExist:
        allAllocation['teamAllocation'] = "Team Allocation Does Not Exist||"+request.data['device_uniqid']+"||"+detailSerializer.data['serial_number']
        return Response(allAllocation)     
    
@api_view(['GET'])
def myDevices(request, uniqid):   
    user = Member.objects.get(uniqid = uniqid) 
    userSerializer = MemberSerializer(user, many=False)
    # return Response(userSerializer.data['uniqid'])
    devices = Allocation.objects.filter(user_allocated = userSerializer.data['uniqid'], status=1)
    serializer =  AllocationSerializer(devices, many=True)
    # return Response(serializer.data)
    i = 0
    allDevices = []
    allAllocation = []
    allAllocation.append(serializer.data)
    data_to_be_displayed = dict()
    # data_to_be_displayed['allocation'] = serializer.data
    while i<len(serializer.data):
            # return Response(assignedPlatformsSerializer.data[i])
            deviceDetails = Device.objects.get(uniqid = serializer.data[i]['device_uniqid'])
            deviceSerializer  = DeviceSerializer(deviceDetails, many=False) 
            
            # deviceType = DeviceType.objects.get(uniqid = deviceSerializer.data['deviceTypeUniqid']) 
            # deviceTypeSerializer = DeviceTypeSerializer(deviceType, many=False)         
            allDevices.append(deviceSerializer.data)           
            i = i + 1 

    data_to_be_displayed['allDevices'] = allDevices
    return Response(data_to_be_displayed) 

 

@api_view(['GET'])
def singleTeamDamagedDevice(request, uniqid):  
    # return Response(uniqid)  
    device = DamagedDevice.objects.filter(device_uniqid = uniqid)
    # return Response(device)
    serializer =  DamagedDeviceSerializer(device, many=True)
  
    return Response(serializer.data) 

@api_view(['GET'])
def userGetUser(request):    
    # device = DamagedDevice.objects.filter( = uniqid)
    # serializer =  DamagedDeviceSerializer(device, many=True)
    return Response(request.data) 
 

@api_view(['POST'])
def userDamagedDevices(request):    
    member = Member.objects.get(uniqid=request.data['user_uniqid'])
    serializer = MemberSerializer(member, many=False)      
    device = Allocation.objects.filter(user_allocated = request.data['user_uniqid'])
    allocation_serializer =AllocationSerializer(device, many=True)
    # return Response(allocation_serializer.data)
    data_to_be_displayed = dict()    
    allDevices = []
    i = 0
    while i<len(allocation_serializer.data):
            # return Response(assignedPlatformsSerializer.data[i])                    
            myDamagedDevices = []
            
            if DamagedDevice.objects.filter(device_uniqid= allocation_serializer.data[i]['device_uniqid']).exists():
                  damagedDevices = DamagedDevice.objects.filter(device_uniqid= allocation_serializer.data[i]['device_uniqid'])
                  damagedDevicesSerializer = DamagedDeviceSerializer(damagedDevices, many=True)
                #   return Response(damagedDevicesSerializer.data[0]['device_uniqid'])
                  myDamagedDevices.append(damagedDevicesSerializer.data)                
                  deviceDetails = Device.objects.get(uniqid = damagedDevicesSerializer.data[i]['device_uniqid'])
                  deviceSerializer  = DeviceSerializer(deviceDetails, many=False) 
                #   return Response(deviceSerializer.data)                           
                  allDevices.append(deviceSerializer.data)
                  data_to_be_displayed['allDevices'] = allDevices 
                  data_to_be_displayed['myDamagedDevices'] = myDamagedDevices
                  
                       
            i = i + 1 
            return Response(data_to_be_displayed) 
   

@api_view(['GET'])
def userTeamDevices(request, user_uniqid):    
    member = Member.objects.get(uniqid=user_uniqid)
    serializer = MemberSerializer(member, many=False)      
    device = TeamAllocation.objects.filter(team_allocated = serializer.data['team'])
    allocation_serializer = TeamAllocationSerializer(device, many=True)
    data_to_be_displayed = dict()
    data_to_be_displayed['teamAllocation'] = allocation_serializer.data
    allTeamDevices = []
    i = 0
    while i<len(allocation_serializer.data):
            # return Response(assignedPlatformsSerializer.data[i])
            deviceDetails = Device.objects.get(uniqid = allocation_serializer.data[i]['device_uniqid'])
            deviceSerializer  = DeviceSerializer(deviceDetails, many=False)            
            allTeamDevices.append(deviceSerializer.data)           
            i = i + 1 
    data_to_be_displayed['allTeamDevices'] = allTeamDevices
    return Response(data_to_be_displayed) 

@api_view(['GET'])
def adminAllLeads(request):
    team_leads = TeamLead.objects.all()
    serializer =  TeamLeadSerializer(team_leads, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminAllUsers(request):
    users = Member.objects.filter(status = 1)
    serializer =  MemberSerializer(users, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminAllUnconfirmedUsers(request):
    users = Member.objects.filter(status = 0)
    serializer =  MemberSerializer(users, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminDamagedDevices(request):
    device = DamagedDevice.objects.filter(status=0)
    serializer = DamagedDeviceSerializer(device, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminAllDevices(request):
    device = Device.objects.all()
    serializer =  DeviceSerializer(device, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminAllDeviceTypes(request):
    device = DeviceType.objects.all()
    serializer = DeviceTypeSerializer(device, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminAllTeams(request):
    teams = Team.objects.all()
    serializer =  TeamSerializer(teams, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def adminSingleTeamDetails(request, uniqid):
    # return Response(uniqid)
    teams = Team.objects.get(uniqid = uniqid)
    serializer =  TeamSerializer(teams, many=False)
    return Response(serializer.data) 


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def addMyDevice(request, format=None):
    # if request.method == 'POST':
    serializer = AllocationSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.uniqid = uuid.uuid4()
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    



@parser_classes([MultiPartParser,FormParser,JSONParser])
def handleAllocation(data):
    return Response(data)

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def postExcelData(request, format=None):
    # if request.method == 'POST':
    
    username = request.data['Email'].split('@')[0]
    # return Response(request.data['Email'])
    
    allMembers = Member.objects.all()
    memberSerializer = MemberSerializer(allMembers, many=True)
    # return Response((memberSerializer.data[1]['email']))
    allEmails = []
    for member in memberSerializer.data:
        allEmails.append(member['email'])
        # return Response(member['email'])
    if request.data['Email'] in allEmails:
        user = Member.objects.get(email = request.data['Email'])
        
    else:
        # return Response("sdfdsfdsf")
        user = Member.objects.create(
        
            email=request.data['Email'],
            full_name=request.data['Full Name'],
            username = username
        )
        user.set_password("PasswordDevice123!")
        user.save()
        username = request.data['Email'].split('@')[0]
        message = f'Hello '+request.data['Full Name']+',\n \n Welcome to the Techno Brain Device Inventory Application. \n  Please Wait for an approval from the Administrator to access your resources. \n \n Regards, \n Device Administrator' 
    #     # return Response(serializer.data['username'])
        send_mail('Welcome to Device Inventory',message,settings.EMAIL_HOST_USER,[request.data['Email']])
    UserSerializer = MemberSerializer(user, many=False)

    
#    ADD DEVICETYPE 
    # return Response(request.data['Device Name'])
    AllDeviceTypes = DeviceType.objects.all()
    allDeviceTypeSerializer = DeviceTypeSerializer(AllDeviceTypes, many=True)
    allNames = []
    for device in allDeviceTypeSerializer.data:
        allNames.append(device['name'])
    # return Response(allNames)   
    if request.data['Device Name'] in allNames:
        # return Response(device['name'])
        checkDeviceName = DeviceType.objects.get(name = request.data['Device Name'])
        checkDeviceSerializer = DeviceTypeSerializer(checkDeviceName, many=False)
        uniqid = str(random.randint(10000000,1000000000000000))
        # return Response(request.data['Serial Number'])
        teamDetails = Team.objects.get(name = request.data['UserTeam'])
        teamDetailsSerializer = TeamSerializer(teamDetails, many=False)
        # return Response(teamDetailsSerializer.data)
        daita = {"serial_number" : request.data['Serial Number'],"deviceTypeUniqid": checkDeviceSerializer.data['uniqid'],"uniqid" : uniqid, "team_assigned_status": 1}
        # return Response(daita['uniqid'])
        deviceSerializer = DeviceSerializer(data=daita)    
        if deviceSerializer.is_valid():        
            deviceSerializer.save()
            
            TAuniqid =  uuid.uuid4()
            teamAllocationData = {"device_uniqid": deviceSerializer.data['uniqid'], "team_allocated": teamDetailsSerializer.data['uniqid'], "uniqid":TAuniqid  }
            # teamAllocatonSerializer = TeamAllocationSerializer(data=teamAllocationData)
            
            # handleAllocation(data=teamAllocationData)
            # return Response(teamAllocationData)
            
            # daita = { "device_uniqid":"786020115890392","team_allocated":"346196f8-8d57-44df-950d-bc18a00ff9e0", "uniqid": "03052d36-46d7-4c22-a767-aa9b6e67b71c" }
            teamAllocationSerializer  = TeamAllocationSerializer(data =teamAllocationData)
            if teamAllocationSerializer.is_valid():
                # teamAllocationSerializer['uniqid'] = uuid.uuid4()
                teamAllocationSerializer.save()
                
                userAllocationData = {"device_uniqid": deviceSerializer.data['uniqid'], "user_allocated": UserSerializer.data['uniqid'], "user_team": teamDetailsSerializer.data['uniqid'], "location": request.data['Device Location']  }
                userAllocatedSerializer = AllocationSerializer(data=userAllocationData)
                if userAllocatedSerializer.is_valid():
                    userAllocatedSerializer.save()
                    return Response(userAllocatedSerializer.data)
                return Response(userAllocatedSerializer.errors)
                # return Response(teamAllocationSerializer.data)
            return Response(teamAllocationSerializer.errors)
        return Response(deviceSerializer.errors)  
        # return Response(checkDeviceSerializer.data)    
        # if Device.objects.get(serial_number = request.data['Serial Number']).exists():
        #     deviceDetails = Device.objects.get(serial_number = request.data['Serial Number'])
        #     deviceDetailsSerializer = DeviceSerializer(deviceDetails, many=False)
        #     return Response(deviceDetailsSerializer.data) 
            
        # else:
        #   return ('does not exists')
           
        
    # elif DeviceType.objects.filter(name__icontains = request.data['Device Name']).exists():
    #     checkSimilarName = DeviceType.objects.filteret(name__icontains = request.data['Device Name'])
    #     checkSimilarSeializer = DeviceTypeSerializer(checkSimilarName, many=True)
    #     return Response(checkSimilarSeializer.data)
    else:
        # if DeviceType.objects.filter(name__icontains = request.data['Device Name']).exists():
        for deviceName in allNames:
            if re.match(deviceName, request.data['Device Name']):
                return Response(deviceName)
            else:
                return Response(request.data['Device Name']+"## Not Found")
                
        # try:
        #     # return Response(request.data['Device Name'])
        #     checkSimilarName = DeviceType.objects.get(name__contains = request.data['Device Name'])
        #     checkSimilarSeializer = DeviceTypeSerializer(checkSimilarName, many=False)
        #     return Response(checkSimilarSeializer.data)
        # except  DeviceType.objects.get(name__contains = request.data['Device Name']).DoesNotExist:
        #     daita = {"name": request.data['Device Name'], "type": request.data['Type'], "brand": request.data['Brand'],"poster_link":"https://cdn.nerdschalk.com/wp-content/uploads/2022/08/set-default-audio-device-windows-11-759x427.png"}
        #     # return Response(daita)
        #     addNewDeviceType = DeviceTypeSerializer(data=daita)
        #     if addNewDeviceType.is_valid():
        #         addNewDeviceType.save()
        #         return Response(addNewDeviceType.data)
        #     UserSeriali 
        # return Response(addNewDeviceType.data)
    # return Response(checkDeviceSerializer.data)
    # return Response(UserSerializer.data['uniqid']) 
        # serializer.uniqid = uuid.uuid4()
    # daita= {"user_allocated": UserSerializer.data['uniqid'], "device_uniqid": }
    # serializer = AllocationSerializer(data=request.data)    
    # if serializer.is_valid():
    #     UserSeriali 
    # return Response(allEmails)
        
    

        

    # #      title = models.CharField(max_length=70)
    # # description = models.CharField(max_length=70)
    # # uniqid = models.CharField(max_length=35, editable=False, default=uuid.uuid4() ,unique=True) 
    # # link = models.CharField(max_length=70)
    # # status = models.IntegerField(default=0)
    # # user_uniqid = models.CharField(max_length=35)
    #     admins = Member.objects.filter(rank = 'admin')
    #     # userSerializer = MemberSerializer(admins, many=True)
    #     # return Response(userSerializer.data)
    #     # notification = Notification.objects.create(
    #     # title  = 'Approve User',
    #     # description = 'A new User needs approval',
    #     # uniqid = uuid.uuid4(),
    #     # link = 'http://localhost:3000/confirm/staff/member',
       
    #     # user_uniqid = models.CharField(max_length=35),
    #     # )
        # message = f'Hello '+request.data['username']+',\n \n Welcome to the Techno Brain Device Inventory Application. \n  Please Wait for an approval from the Administrator to access your resources. \n \n Regards, \n Device Administrator' 
    #     # return Response(serializer.data['username'])
        # send_mail('Welcome to Device Inventory',message,settings.EMAIL_HOST_USER,[request.data['email']])
    #     approvalLink = 'http://localhost:3000/confirm/staff/member/'
    #     adminMessage = f'Hello Admin,\n \n A new User needs to be approved \n \n Please confirm the Member \n \n '+approvalLink+'\n\nRegards,\n Admin'
    #     send_mail('Approve New User',adminMessage,settings.EMAIL_HOST_USER,['deviceinventorytbl@gmail.com'])
        # return user
    
    # if serializer.is_valid():
    #     serializer.uniqid = uuid.uuid4()
    #     serializer.save()
    #     return Response(serializer.data) 
    # return Response(serializer.errors)    


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminConfirmUser(request, format=None):
    
    
    user = Member.objects.get(uniqid=request.data['user_uniqid'])
    daita = {"status":1, "team": request.data['team']}
    second_serializer = MemberSerializer(user, data=daita, partial=True)
    # return Response(second_serializer.data)
    if second_serializer.is_valid():
        second_serializer.uniqid = uuid.uuid4()
        second_serializer.save()
        return Response(second_serializer.data) 
    return Response(second_serializer.errors)
   
   
    
        

# @api_view(['GET'])
# @parser_classes([MultiPartParser,FormParser,JSONParser])
# def leadTeamDevices(request):
#     # if request.method == 'POST':
#     # return Response(request.data)
#     user = Member.objects.get(uniqid = request.data['user_uniqid'])
#     serializer = MemberSerializer(user, many=False)
#     return Response(serializer.data)
#     if serializer.is_valid():
#         serializer.uniqid = random.randint(1000000000, 9999999999)
#         serializer.save()
#         return Response(serializer.data) 
#     return Response(serializer.errors)    

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAddNewDevice(request, format=None):
    # if request.method == 'POST':
    
    requestData = request.data
    requestData['uniqid'] = str(random.randint(10000000,1000000000000000))
    
    requestData['deviceTypeUniqid'] = request.data['name']
    # return Response(requestData)
    serializer = DeviceSerializer(data=requestData)
   
    # serializer.uniqid = uuid.uuid4()
    # return Response(serializer.data)
    if serializer.is_valid():
        
    #     # random.randint(1000000000, 9999999999)
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAddNewDeviceType(request, format=None):
    # if request.method == 'POST':
    # return Response(request.data)
    requestData = request.data
    requestData['uniqid'] = uuid.uuid4()
    # return Response(requestData)
    serializer = DeviceTypeSerializer(data=requestData)
   
    # serializer.uniqid = uuid.uuid4()
    # return Response(serializer.data)
    if serializer.is_valid():
        
    #     # random.randint(1000000000, 9999999999)
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAddNewLead(request, format=None):
    # if request.method == 'POST':
    # print(request.data)
    member = Member.objects.get(uniqid=request.data['user_uniqid'])
    serializer =  MemberSerializer(member, many=False)
    email = serializer.data['email']    
    name = serializer.data['username']    
    team = serializer.data['team']    
    daita = {"rank": "team_lead"}     
    second_serializer = MemberSerializer(member, data=daita, partial=True)
    if second_serializer.is_valid():     
        second_serializer.save()        
    lead_data = {"email" : email, "name" : name, "team" : team}
    lead_serializer = TeamLeadSerializer(data=lead_data)    
    if lead_serializer.is_valid():      
      
        lead_serializer.save()
        return Response(lead_serializer.data)          
    return Response(lead_data)    

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAddNewTeam(request, format=None):
    uniqid = uuid.uuid4()
    # return Response(uniqid)
    daita = {"name" : request.data['name'],"uniqid" : uniqid}
    # return Response(daita['uniqid'])
    serializer = TeamSerializer(data=daita)    
    if serializer.is_valid():        
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def reportDamagedDevice(request, format=None):
    # if request.method == 'POST':
    # return Response(request.data['device_uniqid']) 
    device = Allocation.objects.get(device_uniqid= request.data['device_uniqid'], status=1) 
    serializer = AllocationSerializer(device, many=False)
    # return Response(serializer.data) 
    user_allocated = Member.objects.get(uniqid = serializer.data['user_allocated'])
    user_serializer = MemberSerializer(user_allocated, many=False) 
    # return Response(serializer.data)
   
    daita = {"device_uniqid": request.data['device_uniqid'], "user_uniqid" : user_serializer.data['uniqid'], "explained_issue" : request.data['explained_issue'], "complainant_team": "semantex"}
    # return Response(daita['user_allocated']) 
    second_serializer = DamagedDeviceSerializer(data=daita)
   
    # return Response(daita)
    if second_serializer.is_valid():  
    #     second_serializer.uniqid = uuid.uuid4()
          second_serializer.save()
        
          return Response(second_serializer.data) 
    return Response(serializer.errors)


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def addTeamSharedDevice(request, format=None):
    # if request.method == 'POST':
    serializer = TeamAllocationSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.uniqid = uuid.uuid4()
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAssignTeam(request):
    member = Member.objects.get(uniqid=request.data['user_uniqid'])
    serializer = MemberSerializer(member, many=False)
    # return Response(serializer.data)
    daita = {"team": request.data['team_uniqid']} 
    team = Team.objects.filter(uniqid=request.data['team_uniqid']).count()   
    second_serializer = MemberSerializer(member, data=daita, partial=True)
    if second_serializer.is_valid():    
        second_serializer.save()
        return Response(second_serializer.data) 

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def adminAssignTeamDevice(request):
    # return Response(request.data)
    teamDetails = Team.objects.get(uniqid = request.data['team_allocated'])
    teamSerializer =  TeamSerializer(teamDetails, many=False)
    
    uniqid = uuid.uuid4()
    
   
    # return Response(daita) 
    device = Device.objects.get(uniqid = request.data['device_uniqid'])
    deviceUpdateData = {"team_assigned_status" : 1}
    deviceUpdate = DeviceSerializer(device, data=deviceUpdateData, partial=True)
    if deviceUpdate.is_valid():
        deviceUpdate.save()
        # return Response(deviceUpdate.data)
    # return Response(deviceUpdate.errors)
    status = {"status" : 0}
    # return Response(teamSerializer.data['uniqid']) 
    # teamAllocationExistent = TeamAllocation.objects.filter(team_allocated = request.data['team_allocated'], device_uniqid = request.data['device_uniqid'])
    teamAllocationExistent = TeamAllocation.objects.filter(~Q(team_allocated = request.data['team_allocated']), device_uniqid = request.data['device_uniqid'], status=1)
    # return Response(TeamAllocation.objects.filter(team_allocated = request.data['team_allocated']).count())
    # return Response(teamAllocationExistent.count())
    if teamAllocationExistent.count() > 0:
        teamExistent = TeamAllocationSerializer(teamAllocationExistent, many=True)
        alluniqids = []        
        for allocation in teamExistent.data: 
            # alluniqids.append(allocation['uniqid'])
            # return Response(allocation['uniqid'])
        # return Response(alluniqids)    
            updateAllocation = TeamAllocation.objects.get(uniqid = allocation['uniqid'])
            updateAllocationSerializer = TeamAllocationSerializer(updateAllocation, data=status, partial=True)
            if updateAllocationSerializer.is_valid():
                updateAllocationSerializer.save()
                # return Response(updateAllocationSerializer.data)
            
        daita = {"team_allocated": teamSerializer.data['uniqid'], "device_uniqid": request.data['device_uniqid'], "status": 1 }
        # return Response(daita)
        teamAllocation = TeamAllocationSerializer(data=daita)        
        if teamAllocation.is_valid():
            teamAllocation.uniqid = uuid.uuid4()
            teamAllocation.save()
            return Response(teamAllocation.data) 
    elif TeamAllocation.objects.filter(team_allocated = request.data['team_allocated'], device_uniqid = request.data['device_uniqid'], status=1).count() == 0:      
        # return Response('wHAT You See')
        daita = {"team_allocated": teamSerializer.data['uniqid'], "device_uniqid": request.data['device_uniqid'], "status": 1 }
        teamAllocation = TeamAllocationSerializer(data=daita)
        if teamAllocation.is_valid():
            teamAllocation.uniqid = uuid.uuid4()
            teamAllocation.save()
            return Response(teamAllocation.data) 
        return Response(teamAllocation.errors) 
    # return Response(updateAllocationSerializer.errors)   
    else:
        #  updateAllocation = TeamAllocation.objects.get(uniqid = allocation['uniqid'])
        #  updateAllocationSerializer = TeamAllocationSerializer(updateAllocation, data=status, partial=True)
        #  if updateAllocationSerializer.is_valid():
        #      updateAllocationSerializer.save()
             
        return Response("Already Allocated") 
    
 
@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def leadAddTeamSharedDevices(request):
    member = Member.objects.get(uniqid=request.data["user_uniqid"])
    serializer =  MemberSerializer(member, many=False)
    device = Device.objects.get(uniqid=request.data['device_uniqid'])
    device_serializer = DeviceSerializer(device, many=False)
    daita = {"device_uniqid": request.data['device_uniqid'], "team_allocated": serializer.data['team']} 
    allocation_serializer = TeamAllocationSerializer(data=daita)    
    if allocation_serializer.is_valid():
        allocation_serializer.uniqid = uuid.uuid4()
        allocation_serializer.save()
        return Response(allocation_serializer.data) 
    return Response(allocation_serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def leadAssignNewDevice(request):       
      
    member = Member.objects.get(uniqid=request.data["user_uniqid"])
    serializer =  MemberSerializer(member, many=False)    
   
    # return Response(daita['device_uniqid'])
    try:
        # if Allocation.objects.get(device_uniqid = request.data['device_uniqid'], status=0):
        updateAllocation = Allocation.objects.get(device_uniqid = request.data['device_uniqid'], status=1)
        updateData = {"status": 0}
        updateAllocationSerializer = AllocationSerializer(updateAllocation, data=updateData, partial=True)
        if updateAllocationSerializer.is_valid():  
            updateAllocationSerializer.save()
        daita = {"device_uniqid": request.data['device_uniqid'], "user_allocated": serializer.data['uniqid'], "user_team" : serializer.data['team'], "use" : request.data['use'],"location": request.data['location'], "status": 1 }     
        # return Response(daita)
        allocation_serializer = AllocationSerializer(data=daita)    
        if allocation_serializer.is_valid():            
            allocation_serializer.save()
            device = Device.objects.get(uniqid = request.data['device_uniqid'])
            deviceSerializer = DeviceSerializer(device, many=False)
            data = {
                "resource_assigned_status" : 1
            }
            updateDevicellocationStatus = DeviceSerializer(device, data=data, partial=True)
            if updateDevicellocationStatus.is_valid():
                # serializer.uniqid = uuid.uuid4()
                updateDevicellocationStatus.save()
            devicetype = DeviceType.objects.get(uniqid = deviceSerializer.data['deviceTypeUniqid']) 
            deviceTypeSerializer = DeviceTypeSerializer(devicetype, many=False)
            # return Response(serializer.data['username'])
            # msg_plain = render_to_string('templates/email.html', {'member': serializer.data, "device" : deviceSerializer.data})
            message = f'Hello '+serializer.data['username']+', you have been assigned '+deviceTypeSerializer.data['name']+' device'
            
            send_mail('Device Assigned',message,settings.EMAIL_HOST_USER,[serializer.data['email']])
            return Response(allocation_serializer.data)     
        # else:
        #      return Response('none') 
    except Allocation.DoesNotExist:
        # return Response('none')
        daita = {"device_uniqid": request.data['device_uniqid'], "user_allocated": serializer.data['uniqid'], "user_team" : serializer.data['team'], "use" : request.data['use'],"location": request.data['location'], "status": 1 }     
        # return Response(daita)   
        allocation_serializer = AllocationSerializer(data=daita)    
        if allocation_serializer.is_valid():            
            allocation_serializer.save()
            device = Device.objects.get(uniqid = request.data['device_uniqid'])
            deviceSerializer = DeviceSerializer(device, many=False)
            data = {
                "resource_assigned_status" : 1
            }
            updateDevicellocationStatus = DeviceSerializer(device, data=data, partial=True)
            if updateDevicellocationStatus.is_valid():
                # serializer.uniqid = uuid.uuid4()
                updateDevicellocationStatus.save()
            devicetype = DeviceType.objects.get(uniqid = deviceSerializer.data['deviceTypeUniqid']) 
            deviceTypeSerializer = DeviceTypeSerializer(devicetype, many=False)
            # return Response(serializer.data['username'])
            # msg_plain = render_to_string('templates/email.html', {'member': serializer.data, "device" : deviceSerializer.data})
            message = f'Hello '+serializer.data['username']+', you have been assigned a '+deviceTypeSerializer.data['name']+' device'
            
            send_mail('Device Assigned',message,settings.EMAIL_HOST_USER,[serializer.data['email']])
            return Response(allocation_serializer.data) 
        # return Response(allocation_serializer.errors)  
    
            
    
@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def getDeviceType(request):
    # return Response(request.data)
    device = DeviceType.objects.get(uniqid=request.data['uniqid'])
    serializer =  DeviceTypeSerializer(device, many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def singleDevice(request, uniqid):
    
    device = Device.objects.get(uniqid=uniqid)
    serializer =  DeviceSerializer(device, many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def singleDeviceType(request, uniqid):
    device = DeviceType.objects.get(uniqid=uniqid)
    serializer =  DeviceTypeSerializer(device, many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def singleTeamMember(request, uniqid):
    member = Member.objects.get(uniqid=uniqid)
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def adminSingleTeam(request, uniqid):
    member = Member.objects.filter(team = uniqid)
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def leadMyDevices(request, uniqid):
    devices = Allocation.objects.filter(user_allocated = uniqid)
    serializer = AllocationSerializer(devices, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def leadAllTeamUsersDevices(request):
    device = Allocation.objects.all()
    serializer =  AllocationSerializer(device, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def leadAllTeamUsers(request, uniqid):
    member = Member.objects.get(uniqid=uniqid)
    serializer = MemberSerializer(member, many=False)
    team = Team.objects.get(uniqid=serializer.data['team'])
    teamSerializer = TeamSerializer(team, many=False)
    team_members = Member.objects.filter(team = teamSerializer.data['uniqid'])
    serializer =  MemberSerializer(team_members, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
def leadTeamSharedDevices(request):
    
    # return Response(request.data)
    member = Member.objects.get(uniqid=request.data['user_uniqid'])
    serializer = MemberSerializer(member, many=False) 
    
    # return Response(serializer.data)
    if serializer.data['rank'] == 'admin':
          
        team = Team.objects.get(uniqid = request.data['team_uniqid'])
    else:
         team = Team.objects.get(uniqid = serializer.data['team'])
    
    teamSerializer = TeamSerializer(team, many=False)  
    
    device = TeamAllocation.objects.filter(team_allocated = teamSerializer.data['uniqid'], status=1)
    allocation_serializer = TeamAllocationSerializer(device, many=True)
    # return Response(allocation_serializer.data)
    alldata = {}
    allDevices = []
    alldata['team_details'] = teamSerializer.data
    for allocation in allocation_serializer.data: 
        device = Device.objects.get(uniqid = allocation['device_uniqid'])  
        deviceSerializer = DeviceSerializer(device, many=False)
        allDevices.append(deviceSerializer.data) 
        alldata['allDevices'] = allDevices

        # get_object_or_404(Comment, pk=comment_id) 
        # if Allocation.objects.get(device_uniqid = allocation['device_uniqid']).exists():
        #     allocation = Allocation.objects.get(device_uniqid = allocation['device_uniqid'])  
        # try:
        #        allocation = Allocation.objects.get(device_uniqid = allocation['device_uniqid'])   
        #        allocationSerializer = AllocationSerializer(allocation, many=False)
        #        allDevices.append(allocationSerializer.data)
            #    allDevices.status = "set" 
        # except Allocation.objects.get(device_uniqid = allocation['device_uniqid']).DoesNotExist:
        #         allocation = None             
                  
          
    return Response(alldata)   
    return Response(allocation_serializer.data) 



@api_view(['POST'])
def viewDeviceAllocation(request): 
    try:
        # return Response(request.data)
        allocation = Allocation.objects.get(device_uniqid = request.data['device_uniqid'], status=1)
        serializer = AllocationSerializer(allocation, many=False) 
        # return Response(serializer)
        member = Member.objects.get(uniqid = serializer.data['user_allocated']) 
        memberSerializer = MemberSerializer(member, many=False)
        return Response(memberSerializer.data) 
    except  Allocation.DoesNotExist:
        allocation = None
        return Response("device has not been allocated")
            
    # for member in team_serializer.data:        
    #     request.data["user"] = activity.user
    #     self.create(request, *args, **kwargs)   
    # return Response()         


@api_view(['GET'])
def viewTeamDamagedDevices(request, user_uniqid):      
    member = Member.objects.get(uniqid=user_uniqid)
    serializer = MemberSerializer(member, many=False) 
    # return Response(serializer.data)
    # allDevices=[]
    # if serializer.data['rank'] == 'admin':
    devices = DamagedDevice.objects.all()
    damagedSerializer =  DamagedDeviceSerializer(devices, many=True)
        # allDevices.append(damagedSerializer.data)
    return Response(damagedSerializer.data)
    # return Response(damagedSerializer.errors)  
    # team_members = Member.objects.filter(team=serializer.data['team']) 
    # team_serializer = MemberSerializer(team_members, many=True) 
    # # for member in team_serializer.data:        
    # #     request.data["user"] = activity.user
    # #     self.create(request, *args, **kwargs)   
    # # return Response()         
   
    
    # devices = DamagedDevice.objects.all()
    # damagedSerializer =  DamagedDeviceSerializer(devices, many=True)
    # # return Response(damagedSerializer.data)
    
    # for device in damagedSerializer.data: 
    #     # return Response(device['device_uniqid'])       
    #     deviceDetails = Device.objects.get(uniqid = device['device_uniqid'])
    #     deviceSerializer = DeviceSerializer(deviceDetails, many=False)
    #     allDevices.append(deviceSerializer.data)
        
    #     return Response(allDevices)  
    # return Response(deviceSerializer.errors) 
    
    
    # return Response(serializer.data) 

@api_view(['POST'])
def leadAllTeamMembers(request):
    # return Response(request.data)
    member = Member.objects.get(uniqid=request.data['uniqid'])
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)
    teamMembers = Member.objects.filter(team = serializer.data['team'])
    MemberSerializer =  MemberSerializer(teamMembers, many=True)
    # team = Team.objects.all()
    # serializer =  TeamSerializer(team, many=True)
    
    return Response(MemberSerializer.data) 



    

  