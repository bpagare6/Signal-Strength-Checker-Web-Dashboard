# Generated by Django 3.0.6 on 2021-09-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signalstrength',
            name='locality',
        ),
        migrations.AddField(
            model_name='signalstrength',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
