# Generated by Django 3.2.4 on 2021-06-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DeparmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DeparmentName', models.CharField(max_length=100)),
            ],
        ),
    ]
