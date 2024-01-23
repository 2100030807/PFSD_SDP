# Generated by Django 4.1.7 on 2023-05-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmsapp', '0002_customers_remove_employee_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booknow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('productname', models.CharField(max_length=50, unique=True)),
                ('subject', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField(unique=True)),
                ('enquirytime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'booknow_table',
            },
        ),
    ]
