# Generated by Django 3.2.9 on 2022-11-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_catdisinfo_catsym_dogdisinfo_dogsym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100000)),
                ('prescription', models.CharField(max_length=1000000000)),
            ],
        ),
    ]
