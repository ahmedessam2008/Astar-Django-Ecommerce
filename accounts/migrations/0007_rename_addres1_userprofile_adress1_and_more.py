# Generated by Django 4.0.4 on 2022-06-01 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='addres1',
            new_name='adress1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='addres2',
            new_name='adress2',
        ),
    ]