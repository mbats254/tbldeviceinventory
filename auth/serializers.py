from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.views import APIView
import uuid
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_simplejwt.tokens import 
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from inventory.models import Member, TokenStore, Notification
from inventory.serializers import MemberSerializer
from django.core.mail import send_mail
from django.conf import settings
# from rest_framework.response import Response


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
 
    # @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # self.get_details(token)
        return token
       
       
        # Add custom claims
        # token['username'] = user.username
        # tokenstore = TokenStore.objects.create(
           
            # access_token = token
            # full_name=validated_data['full_name'],
            # username=validated_data['full_name'],
          
          
        # )
  
    # def get_details(token):
    #     access_token_obj = AccessToken(token)
    #     user_id=access_token_obj['username']
    #     return user_id
    
    
    
    
    
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Member.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
 
    
    class Meta:
        model = Member
        fields = ('password', 'password2', 'username', 'email', 'full_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Member.objects.create(
           
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            username = validated_data['username']
          
          
        )

        
        user.set_password(validated_data['password'])
        user.save()
    #      title = models.CharField(max_length=70)
    # description = models.CharField(max_length=70)
    # uniqid = models.CharField(max_length=35, editable=False, default=uuid.uuid4() ,unique=True) 
    # link = models.CharField(max_length=70)
    # status = models.IntegerField(default=0)
    # user_uniqid = models.CharField(max_length=35)
        admins = Member.objects.filter(rank = 'admin')
        # userSerializer = MemberSerializer(admins, many=True)
        # return Response(userSerializer.data)
        # notification = Notification.objects.create(
        # title  = 'Approve User',
        # description = 'A new User needs approval',
        # uniqid = uuid.uuid4(),
        # link = 'http://localhost:3000/confirm/staff/member',
       
        # user_uniqid = models.CharField(max_length=35),
        # )
        message = f'Hello '+validated_data['full_name']+',\n \n Welcome to the Techno Brain Device Inventory Application. \n  Please Wait for an approval from the Administrator to access your resources. \n \n Regards, \n Device Administrator' 
        # return Response(serializer.data['username'])
        send_mail('Welcome to Device Inventory',message,settings.EMAIL_HOST_USER,[validated_data['email']])
        approvalLink = 'http://localhost:3000/confirm/staff/member/'
        adminMessage = f'Hello Admin,\n \n A new User needs to be approved \n \n Please confirm the Member \n \n '+approvalLink+'\n\nRegards,\n Admin'
        send_mail('Approve New User',adminMessage,settings.EMAIL_HOST_USER,['deviceinventorytbl@gmail.com'])
        return user  


class LogoutSerializer(serializers.ModelSerializer):
    # permission_classes = (IsAuthenticated,)
    class Meta:     #instead of meta write Meta (Capital M)
        model = Member
        fields = '__all__'
        
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)