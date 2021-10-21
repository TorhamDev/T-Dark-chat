from django.urls import path
from api import views

urlpatterns = [
    path('',views.index),
    path('api/v1/register/get-valid-code/', views.GetValid_Code.as_view(), name="get valid code"),
    path('api/v1/register/set-user-password/', views.SetUserPasswordCode.as_view(), name="set password"),

]
