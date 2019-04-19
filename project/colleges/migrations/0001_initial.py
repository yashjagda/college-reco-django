# Generated by Django 2.1.4 on 2019-03-12 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('rating', models.CharField(blank=True, max_length=20)),
                ('placements', models.CharField(blank=True, max_length=20)),
                ('fees', models.CharField(blank=True, max_length=20)),
                ('CS_seats', models.CharField(blank=True, max_length=20)),
                ('IT_seats', models.CharField(blank=True, max_length=20)),
                ('EXTC_seats', models.CharField(blank=True, max_length=20)),
                ('Electrical_seats', models.CharField(blank=True, max_length=20)),
                ('chem_seats', models.CharField(blank=True, max_length=20)),
                ('civil_seats', models.CharField(blank=True, max_length=20)),
                ('mechanical_seats', models.CharField(blank=True, max_length=20)),
                ('electronics_seats', models.CharField(blank=True, max_length=20)),
                ('extra_1', models.CharField(blank=True, max_length=200)),
                ('extra_2', models.CharField(blank=True, max_length=200)),
                ('extra_3', models.CharField(blank=True, max_length=200)),
                ('extra_4', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('picsrc', models.CharField(max_length=10000)),
                ('is_picked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.CollegeDetails')),
                ('caste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.Caste')),
                ('f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.Field')),
            ],
        ),
    ]
