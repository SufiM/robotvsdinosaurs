# Generated by Django 4.1.4 on 2022-12-23 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='yyy_position',
            new_name='y_position',
        ),
    ]
