# Generated by Django 2.2 on 2020-07-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0019_auto_20200728_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='nom',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]