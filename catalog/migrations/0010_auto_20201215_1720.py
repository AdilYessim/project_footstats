# Generated by Django 3.1.3 on 2020-12-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201214_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='information',
            field=models.CharField(help_text='Enter description of the player', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='information',
            field=models.CharField(help_text='Enter description of the player', max_length=200),
        ),
    ]
