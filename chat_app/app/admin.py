from django.contrib import admin
from .models import Group,Message
# Register your models here.

@admin.register(Group)
class groupadmin(admin.ModelAdmin):
    list_display=['id','group']

@admin.register(Message)
class groupadmin(admin.ModelAdmin):
    list_display=['id','group','message','timestemp']