# Generated by Django 4.2.3 on 2023-07-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate_App', '0006_remove_apointment_select_price1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_for_contact',
            name='select_price',
        ),
        migrations.RemoveField(
            model_name='request_for_contact',
            name='select_service',
        ),
        migrations.DeleteModel(
            name='HappyCustomers',
        ),
    ]
