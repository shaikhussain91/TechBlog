# Generated by Django 5.1.3 on 2025-02-05 08:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techblog',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]
