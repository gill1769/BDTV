# Generated by Django 3.0.3 on 2022-04-04 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220404_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdetails',
            name='user',
        ),
    ]
