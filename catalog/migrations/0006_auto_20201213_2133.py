# Generated by Django 3.1.3 on 2020-12-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201213_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='coutry',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='player',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
    ]