# Generated by Django 4.0.5 on 2022-06-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_reports_dealer_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reports',
        ),
    ]
