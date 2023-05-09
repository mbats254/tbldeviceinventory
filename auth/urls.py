from django.urls import path
from auth.views import MyObtainTokenPairView, RegisterView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('', views.allViews, name="all_views"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'), 
    path('logout/', LogoutView.as_view(), name='auth_logout'), 
   
    
   
    
    
]