# Generated by Django 4.0 on 2021-12-26 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_alter_participant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
