# Generated by Django 3.2.7 on 2022-01-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduskillprojectapp', '0005_alter_enrollform_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollform',
            name='course',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
