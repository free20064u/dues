# Generated by Django 5.1.2 on 2024-11-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_credit_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='student_image/wbm-logo.png', upload_to='student_image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
