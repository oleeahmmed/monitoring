from django.contrib import admin
from .models import Company, Employee, Screenshot

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'designation', 'is_active')
    list_filter = ('company',)

@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('employee', 'created_at', 'screen_index')
    list_filter = ('employee__company', 'created_at')

admin.site.register(Company)