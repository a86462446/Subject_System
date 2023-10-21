from django.contrib import admin
from .models import course, Student, Student_course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "classs", "required_elective", "credit", "week", "time", "start_session", "end_session")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "student_name", "student_class", 'student_credit')

class Student_courseAdmin(admin.ModelAdmin):
    list_display= ("student_number", "code", "name", "classs", "required_elective", "credit", "week", "time", "start_session", "end_session")


admin.site.register(Student, StudentAdmin)
admin.site.register(course, CourseAdmin)
admin.site.register(Student_course, Student_courseAdmin)