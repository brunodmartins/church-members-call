# Generated by Django 4.2 on 2023-05-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='students',
        ),
        migrations.AddField(
            model_name='classlesson',
            name='students',
            field=models.ManyToManyField(to='calls.student'),
        ),
    ]