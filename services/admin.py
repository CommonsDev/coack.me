from django.contrib import admin

from .models import Service, ServiceCategory, ServiceBadge

class ServiceCategoryAdmin(admin.ModelAdmin):
    model = ServiceCategory
    
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name', 'category', 'website')

class ServiceBadgeAdmin(admin.ModelAdmin):
    model = ServiceBadge


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceBadge, ServiceBadgeAdmin)
