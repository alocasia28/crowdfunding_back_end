# Generated by Django 4.2.3 on 2024-01-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
