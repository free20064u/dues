# Generated by Django 5.1.2 on 2024-11-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_is_active_alter_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=60),
        ),
    ]