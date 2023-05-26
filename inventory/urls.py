from django.urls import path

from . import views

urlpatterns = [
    path("", views.ApiOverview, name="api_overview"),
    path("user/", views.userApiOverview, name="user_api_overview"),
    path("get/user/", views.getUser, name="user_get_user"),
    path("get/device/type/", views.getDeviceType, name="user_get_device_type"),
    path("update/profile/", views.userUpdateProfile, name="user_update_profile"),
    path("forgot/password/", views.userForgetPassword, name="user_forgot_password"),
    path("reset/password/view", views.resetPasswordview, name="user_reset_password_view"),
    path("reset/password/post/", views.resetPasswordPost, name="user_reset_password_post"),
    # path('get/user/', views., name="get_user"), 
    path("user/add/my/device/", views.addMyDevice, name="add_my_new_device"),
    path("user/my/devices/<str:uniqid>", views.myDevices, name="my_devices"),
    path("user/single/device/<str:uniqid>", views.singleDevice, name="single_devices"),
    path("user/single/device/type/<str:uniqid>", views.singleDeviceType, name="single_device_type"),
    path("user/report/damaged/device/", views.reportDamagedDevice, name="report_damaged_device"),
    path("user/damaged/devices/", views.userDamagedDevices, name="userDamagedDevices"),
    path("user/team/devices/<str:user_uniqid>", views.userTeamDevices, name="userTeamDevices"),
    path("user/search/device", views.userSearchDevice, name="userSearchDevice"),
    path("user/notifications/", views.userNotifications, name="userNotifications"),
    path("admin/", views.adminApiOverview, name="admin_api_overview"),
    path("admin/add/new/device/", views.adminAddNewDevice, name="admin_new_device_type"),
    path("admin/add/new/device/type/", views.adminAddNewDeviceType, name="admin_new_device_record"),
    path("admin/confirm/user/", views.adminConfirmUser, name="admin_confirm_user"),
    path("admin/all/devices/", views.adminAllDevices, name="admin_all_devices"),
    path("admin/all/devices/types/", views.adminAllDeviceTypes, name="admin_all_devices_types"),
    path("admin/single/device/allocation/", views.adminSingleDeviceAllocation, name="admin_single_device_allocation"),
    path("admin/all/teams/", views.adminAllTeams, name="admin_all_teams"),
    path("admin/single/team/details/<str:uniqid>", views.adminSingleTeamDetails, name="admin_single_team_details"),
    path("admin/all/unconfirmed/users/", views.adminAllUnconfirmedUsers, name="admin_all_unconfirmed_users"),
    path("admin/all/users/", views.adminAllUsers, name="admin_all_users"),
    path("admin/single/user/devices/", views.adminSingleUserDevices, name="admin_single_user_devices"),
    path("admin/add/team/", views.adminAddNewTeam, name="admin_add_team"),   
    path("admin/add/team/lead/", views.adminAddNewLead, name="admin_add_lead"),   
    path("admin/assign/team/", views.adminAssignTeam, name="admin_assign_team"),   
    path("admin/assign/team/device", views.adminAssignTeamDevice, name="admin_assign_team_device"),   
    path("admin/all/leads/", views.adminAllLeads, name="admin_all_leads"),   
    path("admin/single/team/<str:uniqid>", views.adminSingleTeam, name="admin_single_team"),
    path("admin/view/damaged/devices/", views.adminDamagedDevices, name="admin_damaged_devices"),
    path("lead/", views.leadApiOverview, name="lead_api_overview"),
    path("lead/my/devices/<str:uniqid>", views.leadMyDevices, name="lead_my_devices"),
    path("lead/all/team/users/<str:uniqid>", views.leadAllTeamUsers, name="lead_all_team_users_devices"),
    # path("lead/add/team/shared/devices/", views.leadAddTeamSharedDevices, name="lead_add_team_shared_devices"),
    path("lead/team/shared/devices/", views.leadTeamSharedDevices, name="lead_team_shared_devices"),
    # path("lead/team/team/devices/", views.leadTeamDevices, name="leadTeamDevices"),
    path("lead/view/damaged/devices/<str:user_uniqid>", views.viewTeamDamagedDevices, name="view_team_damaged_devices"),
    path("lead/view/devices/allocation/", views.viewDeviceAllocation, name="view_device_allocation"),
    path("lead/return/device/office/", views.leadReturnDeviceOffice, name="leadReturnDeviceOffice"),
    path("lead/single/damaged/device/<str:uniqid>", views.singleTeamDamagedDevice, name="single_team_damaged_device"),
    # path("lead/add/team/shared/devices/", views.addTeamSharedDevice, name="add_team_shared_device"),
    path("lead/assign/new/device/", views.leadAssignNewDevice, name="lead_assign_new_device"),
    path("lead/all/team/members/", views.leadAllTeamMembers, name="lead_all_team_members"),
    path("lead/single/team/member/<str:uniqid>", views.singleTeamMember, name="single_team_member"),
    path("read/excel/", views.readExcel, name="read_excel"),
    path("post/excel/data/", views.postExcelData, name="post_excel"),
   
    

       
     
 

   
    
    
   
    
    
]