# Generated by Django 3.1.7 on 2021-02-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kathakar',
            name='prasidha_nam',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kathakar',
            name='vriti',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
