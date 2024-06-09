# Generated by Django 5.0.6 on 2024-06-02 11:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0002_recipe_posted_at_recipe_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('review_rating', models.IntegerField(default=0)),
                ('author_rating', models.IntegerField(default=0)),
                ('author_of_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_api.user')),
            ],
        ),
    ]