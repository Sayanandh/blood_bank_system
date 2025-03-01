# Generated by Django 5.1.2 on 2024-11-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_management', '0004_remove_donor_last_donation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='location',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='name',
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
