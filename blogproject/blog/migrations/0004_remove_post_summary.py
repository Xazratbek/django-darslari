# Generated by Django 3.1.14 on 2023-02-10 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='summary',
        ),
    ]
