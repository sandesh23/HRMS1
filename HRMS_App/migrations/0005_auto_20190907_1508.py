# Generated by Django 2.2.4 on 2019-09-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_App', '0004_auto_20190830_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='degree',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=3),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='marital_status',
            field=models.CharField(choices=[('M', 'Married'), ('U', 'Unmarried')], max_length=3),
        ),
        migrations.AlterField(
            model_name='role',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sourceofhire',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
