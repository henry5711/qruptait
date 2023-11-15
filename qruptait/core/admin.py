from django.contrib import admin

# Register your models here.
from .models import TypeUser, User, Asistence
# Register your models here.
admin.site.register([TypeUser, User, Asistence])