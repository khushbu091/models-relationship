# Generated by Django 5.0.3 on 2024-04-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(choices=[('Tata', 'Tata'), ('Audi', 'Audi'), ('creata', 'Create'), ('Nexon', 'Nexon')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FuelTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_name', models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Cng', 'Cng'), ('LPG', 'LPG')], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='stu_aadhar',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]
