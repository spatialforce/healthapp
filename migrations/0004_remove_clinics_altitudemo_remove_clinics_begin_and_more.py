# Generated by Django 5.1.1 on 2024-09-17 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0003_alter_wards_options_alter_wards_case_recor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinics',
            name='altitudemo',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='descriptio',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='draworder',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='end',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='extrude',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='snippet',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='timestamp',
        ),
    ]
