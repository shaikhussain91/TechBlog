# Generated by Django 5.1.3 on 2025-02-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_merge_0003_customuser_0004_alter_techblog_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
