# Generated by Django 4.0 on 2021-12-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_board_board_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='good',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
