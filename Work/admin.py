from django.contrib import admin
from .models import *



class Workadmin(admin.ModelAdmin):

 admin.site.register(Work)