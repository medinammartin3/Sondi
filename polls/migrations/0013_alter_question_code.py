# Generated by Django 4.2.7 on 2024-08-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_question_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
