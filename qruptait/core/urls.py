from django.contrib import admin
from django.urls import path,include
from . import views


#app_name = 'core'
urlpatterns = [
    path("",views.index,name="index"),
    path("users",views.indexUser, name="users"),
    path("users/create",views.formUser, name="users_create"),
    path("users/save",views.createUser, name="users_save"),
    path('asistencia',views.indexasistence, name='asistencia'),
    path('generate_qr/<str:data>/', views.generate_qr, name='generate_qr'),
    path('qr_reader/', views.qr_reader, name='qr_reader'),
    path('create/asistence/<str:user>', views.createAsistence, name='create_asistence'),
]

