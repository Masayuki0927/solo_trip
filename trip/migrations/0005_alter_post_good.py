# Generated by Django 4.0 on 2021-12-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_post_good'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]