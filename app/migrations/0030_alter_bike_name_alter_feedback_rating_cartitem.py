# Generated by Django 4.2.16 on 2024-11-30 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0029_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Оценка сайта'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
