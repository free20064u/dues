# Generated by Django 5.1.2 on 2024-11-27 13:23

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='profile/wbm-logo.png', null=True, upload_to='profile'),
        ),
    ]