# Generated by Django 3.0.11 on 2020-12-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_shorturl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
