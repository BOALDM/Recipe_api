# Generated by Django 5.0.6 on 2024-06-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0003_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
