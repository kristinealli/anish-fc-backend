# Generated by Django 4.2.16 on 2024-11-25 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_deck_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercardprogress',
            name='card_due_for_review',
        ),
    ]