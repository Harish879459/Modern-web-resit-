# Generated by Django 3.0.8 on 2020-12-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('shoe_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='static/images/shoe/')),
            ],
            options={
                'db_table': 'shoe',
            },
        ),
    ]
