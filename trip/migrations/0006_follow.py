# Generated by Django 4.0 on 2021-12-24 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_alter_post_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='do_follow_user', to='trip.customuser')),
                ('followerd_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accept_follow_user', to='trip.customuser')),
            ],
        ),
    ]
