# Generated by Django 4.0 on 2021-12-22 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Person',
            new_name='person',
        ),
    ]
