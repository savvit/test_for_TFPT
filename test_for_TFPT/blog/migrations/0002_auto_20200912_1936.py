# Generated by Django 3.1.1 on 2020-09-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='testslug', max_length=250, unique=True, verbose_name='URL поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='testslug', max_length=1000),
        ),
    ]