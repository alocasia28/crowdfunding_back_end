# Generated by Django 4.2.3 on 2024-01-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_pledge_supporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
