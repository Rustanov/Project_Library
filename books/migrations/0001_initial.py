# Generated by Django 3.0.11 on 2020-11-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('file', models.FileField(upload_to='all_books/')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='Обложка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('author', models.CharField(max_length=150)),
                ('page', models.IntegerField(verbose_name='Страницы')),
                ('isbn', models.SmallIntegerField(unique=True, verbose_name='ISBN')),
                ('publisher', models.CharField(max_length=250, verbose_name='Издатель')),
                ('year', models.DateField(verbose_name='Год')),
                ('lanquages', models.CharField(max_length=50, verbose_name='Язык')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Category')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]