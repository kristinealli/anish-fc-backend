# Generated by Django 4.2.16 on 2024-11-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_remove_deck_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
