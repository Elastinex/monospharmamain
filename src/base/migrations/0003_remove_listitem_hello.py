# Generated by Django 3.0.8 on 2020-08-12 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_listitem_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='hello',
        ),
    ]
