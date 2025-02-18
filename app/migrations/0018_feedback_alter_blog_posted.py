# Generated by Django 4.2.16 on 2024-11-18 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_blog_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rating', models.IntegerField(verbose_name='Оценка сайта')),
                ('comments', models.TextField(verbose_name='Комментарии')),
                ('subscribe', models.BooleanField(default=False, verbose_name='Подписаться на новости')),
                ('suggestions', models.TextField(blank=True, null=True, verbose_name='Предложения')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 18, 13, 33, 6, 641255), verbose_name='Опубликована'),
        ),
    ]
