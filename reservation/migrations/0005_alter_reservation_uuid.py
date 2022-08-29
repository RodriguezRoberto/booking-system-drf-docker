# Generated by Django 4.0.6 on 2022-08-29 03:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_reservation_created_at_reservation_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('27c477bb-311c-4047-a59d-cd6729af3a99'), editable=False, unique=True),
        ),
    ]