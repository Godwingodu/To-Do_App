# Generated by Django 3.2.12 on 2023-02-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]