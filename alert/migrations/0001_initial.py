# Generated by Django 3.0 on 2019-12-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=50)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=50)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]