# Generated by Django 5.1.7 on 2025-03-19 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatarId', models.CharField(max_length=100)),
                ('avatarImageURL', models.TextField()),
                ('avatarName', models.CharField(max_length=100)),
                ('avatarVideoURL', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShortVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('hook', models.CharField(max_length=100)),
                ('videoURL', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avatarId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='short_video', to='api.avatar')),
            ],
        ),
    ]
