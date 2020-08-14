# Generated by Django 3.0.8 on 2020-08-11 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20200811_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='poll.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
            preserve_default=False,
        ),
    ]
