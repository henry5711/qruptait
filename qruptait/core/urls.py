from django.contrib import admin
from django.urls import path,include
from . import views


#app_name = 'core'
urlpatterns = [
    path("",views.index,name="index"),
    path("users",views.indexUser, name="users"),
    path('asistencia',views.indexasistence, name='asistencia'),
    path('generate_qr/<str:data>/', views.generate_qr, name='generate_qr'),
]

