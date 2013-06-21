from django.contrib import admin

from .models import Profile, UserService

class UserService(admin.TabularInline):
    model = UserService
    
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [UserService]

admin.site.unregister(Profile)    
admin.site.register(Profile, ProfileAdmin)

