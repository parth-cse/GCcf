# Generated by Django 4.2.6 on 2023-11-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_completed_gen_ai'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='eligible_for_certificate',
            field=models.BooleanField(default=False),
        ),
    ]
