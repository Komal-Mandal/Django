from django.contrib import admin
from student.models import profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','roll')
    
admin.site.register(profile,ProfileAdmin)