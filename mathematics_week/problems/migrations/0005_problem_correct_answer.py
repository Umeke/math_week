# Generated by Django 5.1.4 on 2024-12-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_remove_problem_correct_answer_problem_admin_only_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='correct_answer',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
    ]
