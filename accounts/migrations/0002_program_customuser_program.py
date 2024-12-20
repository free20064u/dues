# Generated by Django 5.1.2 on 2024-11-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=60)),
                ('created', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='program',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.program'),
        ),
    ]
