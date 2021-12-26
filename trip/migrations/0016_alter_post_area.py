# Generated by Django 4.0 on 2021-12-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0015_alter_post_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='area',
            field=models.CharField(blank=True, choices=[('hokkaido', '北海道'), ('okinawa', '沖縄'), ('東北', '東北'), ('関東', '関東'), ('東海', '東海'), ('北陸', '北陸'), ('近畿', '近畿'), ('山陽・山陰', '山陽・山陰'), ('四国', '四国'), ('海外', '海外')], default=None, max_length=100, null=True),
        ),
    ]
