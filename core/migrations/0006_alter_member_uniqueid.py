# Generated by Django 5.1 on 2024-08-20 14:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_member_uniqueid_alter_member_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='uniqueID',
            field=models.CharField(blank=True, default=uuid.UUID('9f75ef20-6e85-4c16-9a49-5b894fa9ff9f'), max_length=36),
        ),
    ]
