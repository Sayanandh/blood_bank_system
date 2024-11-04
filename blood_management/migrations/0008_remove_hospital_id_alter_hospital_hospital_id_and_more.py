# Generated by Django 5.1.2 on 2024-11-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_management', '0007_alter_hospital_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]