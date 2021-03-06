# Generated by Django 4.0.3 on 2022-04-19 02:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(default='', max_length=1000)),
                ('user', models.CharField(max_length=1000)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
