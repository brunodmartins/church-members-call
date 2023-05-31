from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ClassLesson(models.Model):
    date = models.DateTimeField("class date")
    classObj = models.ForeignKey(Class, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ForeignKey(Student, on_delete=models.PROTECT)