# Generated by Django 5.0.6 on 2024-06-02 11:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0004_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('comment_posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_rating', models.IntegerField(default=0)),
                ('comment_reaction', models.IntegerField(default=0)),
                ('author_of_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_api.user')),
                ('comment_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_api.recipe')),
            ],
        ),
    ]
