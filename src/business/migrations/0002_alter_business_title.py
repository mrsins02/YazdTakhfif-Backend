# Generated by Django 3.2.12 on 2023-07-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]