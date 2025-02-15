# Generated by Django 5.1.1 on 2024-09-16 17:32

import subgenres.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subgenres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subgenre',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='subgenre-icons', validators=[subgenres.validators.MaxSizeValidator(1048576, 'A imagem não pode ter mais de 1MB.')], verbose_name='Ícone'),
        ),
    ]
