# Generated by Django 3.0.8 on 2020-08-11 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20200722_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_answer_right', models.BooleanField(default=False, verbose_name='Is answer right')),
            ],
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'Санал асуулга', 'verbose_name_plural': 'Санал асуулга'},
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_one',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_one_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_three',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_three_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_two',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='option_two_count',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='question',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_answer_right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Right')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Question')),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Answer'),
        ),
    ]
