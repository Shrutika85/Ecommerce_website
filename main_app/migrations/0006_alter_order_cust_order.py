# Generated by Django 4.0.2 on 2022-05-11 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_order_items_remove_cart_item_modified_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cust_order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.cart'),
        ),
    ]
