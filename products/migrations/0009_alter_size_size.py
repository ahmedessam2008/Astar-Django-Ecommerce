# Generated by Django 4.0.4 on 2022-05-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(blank=True, choices=[('small', 'small'), ('larg', 'larg'), ('medium', 'medium'), ('xl', 'xl'), ('2xl', '2xl'), ('big', 'big')], max_length=50, null=True),
        ),
    ]
