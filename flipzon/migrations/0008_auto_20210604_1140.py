# Generated by Django 3.1.7 on 2021-06-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipzon', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]