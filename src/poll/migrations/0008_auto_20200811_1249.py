# Generated by Django 3.0.8 on 2020-08-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_auto_20200811_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_answer_right',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is answer right'),
        ),
    ]
