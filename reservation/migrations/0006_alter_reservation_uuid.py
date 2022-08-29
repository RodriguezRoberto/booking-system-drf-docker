# Generated by Django 4.0.6 on 2022-08-29 03:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reservation_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('64189138-293b-4667-9aad-a3a268bcf6ac'), editable=False, unique=True),
        ),
    ]