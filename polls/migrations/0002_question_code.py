# Generated by Django 4.2.7 on 2024-08-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]