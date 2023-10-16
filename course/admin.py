from django.contrib import admin
from .models import course, D1051831_course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "classs", "required_elective", "credit", "time")

admin.site.register(course, CourseAdmin)

class D1051831Admin(admin.ModelAdmin):
    list_display = ("code", "name", "classs", "required_elective", "credit", "time")

admin.site.register(D1051831_course, D1051831Admin)