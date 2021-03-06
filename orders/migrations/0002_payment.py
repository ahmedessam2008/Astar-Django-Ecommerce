# Generated by Django 4.0.4 on 2022-06-10 00:08

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_adress', models.CharField(blank=True, max_length=150)),
                ('shipping_mobile', models.CharField(blank=True, max_length=150)),
                ('pyment_method', models.CharField(blank=True, choices=[('paypal', 'paypal'), ('cod', 'cod'), ('credit', 'credit'), ('bank', 'bank')], max_length=100)),
                ('card_number', creditcards.models.CardNumberField(max_length=25)),
                ('expired', creditcards.models.CardExpiryField()),
                ('security_code', creditcards.models.SecurityCodeField(max_length=4)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
