# Generated by Django 3.1 on 2021-06-19 13:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import treewidget.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=255, verbose_name='ProductForm ')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний хэлбэр',
                'ordering': ['form_name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255, verbose_name='Type of product')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний төрөл',
                'ordering': ['type_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Нэр')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Код')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=400, null=True, verbose_name='Тайлбар')),
                ('is_top', models.BooleanField(default=False, verbose_name='Онцлох эсэх')),
                ('is_active', models.BooleanField(default=True, verbose_name='Идэвхитэй эсэх')),
                ('photo', models.ImageField(blank=True, upload_to='product', verbose_name='Зураг')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', treewidget.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory', verbose_name='Толгой ангилал')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний ангилал',
                'verbose_name_plural': 'Бүтээгдэхүүний ангилал',
                'ordering': ['tree_id', 'mptt_level', 'lft', '-rght'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True, verbose_name='Бүтээгдэхүүн дотоод код')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product name ')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Product Slug')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('instructions', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ingredients', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('warnings', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/product/image/', verbose_name='Picture')),
                ('is_product_new', models.BooleanField(blank=True, default=False, null=True)),
                ('international_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product intertational name')),
                ('link', models.CharField(blank=True, max_length=355, null=True, verbose_name='Link to emonos')),
                ('daatgal', models.BooleanField(blank=True, default=False, help_text='Бүтээгдэхүүн даатгалд хамрагддаг бол зөв болгоно уу', null=True)),
                ('jor', models.BooleanField(blank=True, default=False, help_text='Бүтээгдэхүүн жортой бол зөвлөн үү', null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='product.ProductCategory', verbose_name='Ангилалууд')),
                ('productForm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productform', verbose_name='ProductForm')),
                ('producttype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.type', verbose_name='producttype')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүн',
                'verbose_name_plural': 'Бүтээгдэхүүн',
                'ordering': ['name'],
            },
        ),
    ]
