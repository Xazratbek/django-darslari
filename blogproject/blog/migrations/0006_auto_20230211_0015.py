# Generated by Django 3.1.14 on 2023-02-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(max_length=400),
        ),
    ]
