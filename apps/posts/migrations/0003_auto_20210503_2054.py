# Generated by Django 2.2 on 2021-05-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост'},
        ),
    ]
