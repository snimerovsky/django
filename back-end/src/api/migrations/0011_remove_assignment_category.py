# Generated by Django 2.1.5 on 2019-05-06 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190506_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='category',
        ),
    ]
