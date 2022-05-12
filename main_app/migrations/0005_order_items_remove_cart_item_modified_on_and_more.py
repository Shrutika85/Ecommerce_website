# Generated by Django 4.0.2 on 2022-05-11 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('order_id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('orderedon', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='modified_on',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_prod',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='cust_order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.cart'),
        ),
        migrations.DeleteModel(
            name='order_details',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.order'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_prod',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.customer'),
        ),
    ]
