# Generated by Django 4.0.4 on 2022-05-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centraal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='u_trello_card_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]