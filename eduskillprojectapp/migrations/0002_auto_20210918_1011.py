# Generated by Django 3.2.7 on 2021-09-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduskillprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryform',
            name='hear',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enquiryform',
            name='mode_training',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enquiryform',
            name='other',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]