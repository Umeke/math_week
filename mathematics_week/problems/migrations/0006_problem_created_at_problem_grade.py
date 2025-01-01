# Generated by Django 5.1.4 on 2024-12-30 14:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_problem_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='grade',
            field=models.IntegerField(choices=[(5, '5-сынып'), (6, '6-сынып'), (7, '7-сынып'), (8, '8-сынып'), (9, '9-сынып'), (10, '10-сынып'), (11, '11-сынып')], default=5),
        ),
    ]
