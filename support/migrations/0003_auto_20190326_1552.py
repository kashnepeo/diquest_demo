# Generated by Django 2.1.5 on 2019-03-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20190326_1538'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShowML',
        ),
        migrations.DeleteModel(
            name='ShowMorpheme',
        ),
        migrations.DeleteModel(
            name='ShowRTC',
        ),
    ]
