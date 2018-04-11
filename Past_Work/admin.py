from django.contrib import admin
from .models import *



class Past_Workadmin(admin.ModelAdmin):

 admin.site.register(Past_Work)