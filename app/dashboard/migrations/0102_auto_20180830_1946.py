# Generated by Django 2.0.7 on 2018-08-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0101_auto_20180829_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='expires_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]