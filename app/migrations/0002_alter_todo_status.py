# Generated by Django 3.2.12 on 2023-02-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('PENDING', 'PENDING')], max_length=10),
        ),
    ]
