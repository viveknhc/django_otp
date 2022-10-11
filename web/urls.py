from django.urls import path
from  . import views

app_name='web'

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
]