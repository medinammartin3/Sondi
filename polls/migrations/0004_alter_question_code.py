# Generated by Django 4.2.7 on 2024-08-13 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]