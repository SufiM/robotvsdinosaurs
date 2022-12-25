# Generated by Django 4.1.4 on 2022-12-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_dinosaur_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.IntegerField(choices=[(0, 'Set Robot'), (1, 'Set Dinosaur'), (2, 'Playing'), (3, 'Game finished')], default=0),
        ),
    ]
