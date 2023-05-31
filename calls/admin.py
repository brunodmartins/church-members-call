from django.contrib import admin

from .models import Teacher, Class, Student, ClassLesson

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(ClassLesson)
