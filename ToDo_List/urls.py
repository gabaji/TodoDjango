from django.contrib import admin
from django.urls import path,include
from ToDo_List import views

app_name = 'ToDo_List'

urlpatterns = [
    path('login/',views.login_func),
    path('logout/',views.logout_func),
    path('new/',views.newToDo),
    # path('list/')

]
