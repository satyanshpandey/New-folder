from django.contrib import admin

from .models import Course, Subject, Teacher, Student, Profile , StudentRegionNorth, StudentRegionSouth


# Register your models here.
admin.site.register(StudentRegionNorth)
admin.site.register(StudentRegionSouth)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Profile)