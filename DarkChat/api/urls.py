from django.urls import path
from api import views

urlpatterns = [
    path('',views.index),
    path('api/v1/register/get-valid-code/', views.GetValid_Code.as_view(), name="get valid code"),
    path('api/v1/register/set-user-password/', views.SetUserPasswordCode.as_view(), name="set password"),
    path('api/v1/messages/send', views.SendMessage.as_view(), name="send message"),
    path('api/v1/messages/get-last-message', views.GetLastMessage.as_view(), name="get last message"),
    path('api/v1/users/upadte-user-code', views.UpadteUserCode.as_view(), name="upadte user code"),
    path('api/v1/users/upadte-user-token', views.UpadteToken.as_view(), name="upadte user token"),
    path('api/v1/users/check-user-alive', views.CheckuserIsAlive.as_view(), name="check that the user is alive"),
]
