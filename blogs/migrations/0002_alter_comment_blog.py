# Generated by Django 5.0.4 on 2024-05-09 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blog'),
        ),
    ]
