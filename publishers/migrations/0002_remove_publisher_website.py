# Generated by Django 5.1.1 on 2024-09-08 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
    ]
