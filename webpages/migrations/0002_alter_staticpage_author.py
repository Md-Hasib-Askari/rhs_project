# Generated by Django 3.2.7 on 2021-09-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='author',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]
