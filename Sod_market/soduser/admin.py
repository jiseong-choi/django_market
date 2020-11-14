from django.contrib import admin
from .models import Soduser
# Register your models here.

class SoduserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    
admin.site.register(Soduser, SoduserAdmin)