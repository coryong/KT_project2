# Generated by Django 4.2.7 on 2024-01-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommend', '0002_remove_recommend_env_recommend_env'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommend',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recommend_images/'),
        ),
    ]
