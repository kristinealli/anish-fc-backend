# Generated by Django 4.2.16 on 2024-11-24 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_card_deck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='owner',
        ),
    ]
