# Generated by Django 2.2 on 2019-07-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190723_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sgender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'Female'), ('N', 'None')], max_length=6),
        ),
    ]