from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'department', 'position', 'is_active']
    list_filter = ['department', 'is_active', 'hire_date']
    search_fields = ['first_name', 'last_name', 'email', 'employee_id']
    list_per_page = 25
