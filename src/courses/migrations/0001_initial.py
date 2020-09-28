# Generated by Django 3.1 on 2020-09-28 01:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(max_length=200, null=True, verbose_name='Description')),
                ('image', models.ImageField(default='cat_images/default.png', upload_to='cat_images', verbose_name='Picture')),
                ('price', models.CharField(default='₮', max_length=150, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Course category',
                'verbose_name_plural': 'Course category',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now=True, verbose_name='Created_on')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by ')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subject',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name=' Lesson title')),
                ('slug', models.SlugField()),
                ('video_id', models.FileField(blank=True, null=True, upload_to='course_video', verbose_name='Upload video')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('position', models.IntegerField(verbose_name='Lesson position')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_file')),
                ('photo', models.FileField(blank=True, null=True, upload_to='course_image')),
                ('is_active', models.BooleanField(verbose_name='Register activated')),
                ('start_at', models.DateTimeField(help_text='0000-00-00 00:00:00 форматтай байна', null=True, verbose_name='Start_at')),
                ('state', models.CharField(choices=[('started', 'Lesson started'), ('done', 'Lesson over')], default='started', max_length=100, verbose_name='State')),
                ('youtube_code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Youtubecode')),
                ('embedurl', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lesson',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Course_category', to='courses.coursecategory'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
    ]
