from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "Matric_number", "department"]
    list_filter = ["name", "Matric_number", "department"]
    search_fields = ["name", "Matric_number"]

admin.site.register(Student, StudentAdmin)