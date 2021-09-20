# Generated by Django 3.2.7 on 2021-09-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionnotice',
            name='admission_notice_author',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='jobsboard',
            name='job_author',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='post_author',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='notice_author',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
