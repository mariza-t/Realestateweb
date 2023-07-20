# Generated by Django 4.2.3 on 2023-07-09 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flname', models.CharField(max_length=50)),
                ('qoutetitle', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=150)),
                ('profession', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgno', models.IntegerField()),
                ('pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Property_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('hometype', models.CharField(max_length=80)),
                ('homediscription', models.TextField(max_length=180)),
                ('Address', models.TextField(max_length=100)),
                ('postedby', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('price_space', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quick_appoitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_no', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('price_selection', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Readme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('readme', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=50)),
                ('services_discription', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HappyCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerno', models.IntegerField()),
                ('Comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RealEstate_App.comment')),
            ],
        ),
    ]
