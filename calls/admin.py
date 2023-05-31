from django.contrib import admin

from .models import Teacher, SchoolClass, Student, ClassReport

admin.site.register(Teacher)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(ClassReport)
