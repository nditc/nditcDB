# Generated by Django 5.1 on 2024-08-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='uniqueID',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='year',
            field=models.IntegerField(choices=[(2025, '2023-24'), (2024, '2022-23'), (2023, '2021-22'), (2022, '2020-21'), (2021, '2019-20'), (2020, '2018-19'), (2019, '2017-18')]),
        ),
    ]