# Generated by Django 4.2.16 on 2024-11-05 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 5, 23, 50, 2, 229886), verbose_name='Опубликована'),
        ),
    ]
