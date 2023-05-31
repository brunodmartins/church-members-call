from django.db import models


class SchoolClass(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    school_class = models.ManyToManyField(SchoolClass)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ClassReport(models.Model):
    date = models.DateField("Class date")
    school_class = models.ForeignKey(SchoolClass, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
