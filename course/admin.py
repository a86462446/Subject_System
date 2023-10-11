from django.contrib import admin
from .models import course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "classs", "required_elective", "credit")

admin.site.register(course, CourseAdmin)