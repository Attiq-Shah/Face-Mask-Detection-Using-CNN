# Generated by Django 3.1.7 on 2023-01-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0002_remove_mymodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
