# Generated by Django 4.0.3 on 2022-03-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='height',
            field=models.IntegerField(default=0),
        ),
    ]
