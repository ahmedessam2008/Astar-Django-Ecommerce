# Generated by Django 4.0.4 on 2022-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_post',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
