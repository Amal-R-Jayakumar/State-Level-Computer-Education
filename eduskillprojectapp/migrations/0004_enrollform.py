# Generated by Django 3.2.7 on 2022-01-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduskillprojectapp', '0003_alter_enquiryform_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]
