# Generated by Django 4.2 on 2023-05-31 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_remove_classlesson_students_classlesson_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Class date')),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='school_class',
        ),
        migrations.RenameModel(
            old_name='Class',
            new_name='SchoolClass',
        ),
        migrations.DeleteModel(
            name='ClassLesson',
        ),
        migrations.AddField(
            model_name='classreport',
            name='school_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='calls.schoolclass'),
        ),
        migrations.AddField(
            model_name='classreport',
            name='students',
            field=models.ManyToManyField(to='calls.student'),
        ),
        migrations.AddField(
            model_name='classreport',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='calls.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='school_class',
            field=models.ManyToManyField(to='calls.schoolclass'),
        ),
    ]
