# Generated by Django 4.2.1 on 2023-05-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('mobile_operator_code', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=50)),
            ],
        ),
    ]
