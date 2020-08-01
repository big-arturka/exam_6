# Generated by Django 2.2 on 2020-08-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]