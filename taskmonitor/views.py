from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes ,renderer_classes
from rest_framework.response import Response
from .serializers import TaskMonitorSerializer, TaskSerializer
from .models import User,  Task, TaskMonitor
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, JSONParser, FileUploadParser
from django.http import JsonResponse
import uuid
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'user_routes-GET':'/app/user/',
        'admin_routes-GET' :'/app/admin/',
        'planning_routes-GET':'/app/planning/',            

    }
    return Response(api_urls)


@api_view(['GET'])
def userApiOverview(request):
     
    api_urls = {
        'all_completed-jobs--GET':'/app/user/all/completed/jobs',
        'all_completed-jobs-GET' :'/app/user/all/hibernated/jobs',
        'all_pending-jobs-GET':'/app/user/all/pending/jobs',
        'single-job-GET':'/app/single/job/<str:uniqid>',       

    }
    return Response(api_urls)



# @api_view(['GET'])
# def createTask(request):
#     task = Task.objects.all()
#     jobCardSerializer = JobCardSerializer(jobCards, many=True)
    
#     return Response(jobCardSerializer.data)



@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def createTask(request, format=None):
    # if request.method == 'POST':
    # return Response(request.data['userUniqid'])
    uniqid = uuid.uuid4()
    # return Response(uniqid)
    daita = {"taskName" : request.data['taskName'], "taskType" : request.data['taskType'], "uniqid": uniqid}
    # return Response(daita)
    serializer =  TaskSerializer(data=daita)
    # return Response(serializer.da)
    
    if serializer.is_valid():
        
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def assignTask(request, format=None):
    # if request.method == 'POST':
    # return Response(request.data['userUniqid'])
    uniqid =uuid.uuid4()
    # return Response(uniqid)
    daita = {"taskuniqid" : request.data['taskuniqid'], "resourceUniqid" : request.data['resourceUniqid'],"endTime": request.data['endTime'], "uniqid": uniqid}
    # return Response(daita)
    serializer =  TaskMonitorSerializer(data=daita)
    # return Response(serializer.da)
    
    if serializer.is_valid():
        
        serializer.save()
        return Response(serializer.data) 
    return Response(serializer.errors)    

@api_view(['GET'])
def allTasks(request):
    task = Task.objects.filter(status = 0)    
    serializer =  TaskSerializer(task, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def allMyTasks(request, resourceuniqid):
    TaskMonitor = TaskMonitor.objects.filter(resourceUniqid = resourceuniqid)    
    serializer =  TaskMonitorSerializer(task, many=True)
    allPlatforms = []
    architectures = []
    daita = serializer
    # return Response(assignedPlatformsSerializer.data)
    i = 0
    while i<len(serializer.data):
        # return Response(assignedPlatformsSerializer.data[i])
        task = Task.objects.get(uniqid = serializer.data[i]['taskuniqid'])
        platformSerializer  = TaskSerializer(task, many=False)
        data_to_be_displayed = dict()
        
        architectures.append(TaskSerializer.data[i]['architecture'])
        data_to_be_displayed['architectures'] = architectures
        allPlatforms.append(platformSerializer.data)
        i = i + 1
    data_to_be_displayed['allPlatforms'] = allPlatforms   
    return Response(data_to_be_displayed)   


@api_view(['GET'])
def singleTask(request, uniqid):
    task = Task.objects.get(uniqid=uniqid)    
    serializer =  TaskSerializer(task, many=False)
    return Response(serializer.data)   
 