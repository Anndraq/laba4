# Generated by Django 4.2.16 on 2024-11-22 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_feedback_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 22, 20, 43, 40, 622531), verbose_name='Опубликована'),
        ),
    ]
