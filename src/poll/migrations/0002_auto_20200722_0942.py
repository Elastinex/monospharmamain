# Generated by Django 3.0.7 on 2020-07-22 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ['question'], 'verbose_name': 'Санал асуулга', 'verbose_name_plural': 'Санал асуулга'},
        ),
    ]
