# Generated by Django 4.0.4 on 2024-11-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_usercardprogress_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercardprogress',
            name='last_review_result',
            field=models.BooleanField(default=False),
        ),
    ]
