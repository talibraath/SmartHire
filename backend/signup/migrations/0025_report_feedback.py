# Generated by Django 5.0.6 on 2024-12-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0024_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='feedback',
            field=models.TextField(default='No feedback provided'),
            preserve_default=False,
        ),
    ]
