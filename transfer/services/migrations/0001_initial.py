# Generated by Django 3.1.3 on 2021-01-16 11:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('full_description', ckeditor.fields.RichTextField(verbose_name='Полное описание')),
                ('pictogram', models.ImageField(upload_to='services', verbose_name='Пиктограмма')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='CarouselInner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='setting', verbose_name='Изображение')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Вкладка',
                'verbose_name_plural': 'Вкладки карусели',
            },
        ),
    ]
