# Generated by Django 5.1.4 on 2024-12-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_problem_created_at_problem_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='problem_images/'),
        ),
    ]
