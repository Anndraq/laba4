# Generated by Django 4.2.16 on 2024-11-30 03:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 30, 6, 23, 31, 892352), verbose_name='Опубликована'),
        ),
    ]
