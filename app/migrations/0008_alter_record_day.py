# Generated by Django 4.1.6 on 2023-02-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_record_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='day',
            field=models.DateField(),
        ),
    ]
