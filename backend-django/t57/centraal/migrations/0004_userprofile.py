# Generated by Django 4.0.4 on 2022-05-23 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centraal', '0003_url_u_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_trello_api_key', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('p_trello_api_secret', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('p_trello_token', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('p_trello_token_secret', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('p_trello_default_list', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('p_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
