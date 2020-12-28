# Generated by Django 3.0.8 on 2020-12-24 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('shoe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe.Shoe')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
