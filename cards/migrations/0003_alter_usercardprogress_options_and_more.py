# Generated by Django 4.0.4 on 2024-11-16 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_remove_profile_decks_in_curriculum_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercardprogress',
            options={},
        ),
        migrations.AlterModelOptions(
            name='userdeck',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='usercardprogress',
            name='cards_userc_user_id_f6f4db_idx',
        ),
        migrations.RemoveIndex(
            model_name='usercardprogress',
            name='cards_userc_user_id_72c33c_idx',
        ),
        migrations.RemoveIndex(
            model_name='userdeck',
            name='cards_userd_user_id_54386f_idx',
        ),
        migrations.RemoveIndex(
            model_name='userdeck',
            name='cards_userd_user_id_00e3d7_idx',
        ),
        migrations.RenameField(
            model_name='userdeck',
            old_name='last_reviewed',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='userdeck',
            old_name='is_favorite',
            new_name='is_owner',
        ),
        migrations.AlterUniqueTogether(
            name='usercardprogress',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='decks_in_curriculum',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='cards_mastered',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='correct_answers',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='custom_notes',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='incorrect_answers',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='next_review_date',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='review_streak',
        ),
        migrations.RemoveField(
            model_name='userdeck',
            name='total_reviews',
        ),
        migrations.AddField(
            model_name='profile',
            name='chosen_decks',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='cards.deck'),
        ),
        migrations.AlterField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck_cards', to='cards.deck'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='decks', to='cards.tag'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferred_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usercardprogress',
            name='box_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usercardprogress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usercardprogress',
            name='last_reviewed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usercardprogress',
            name='next_review_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userdeck',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_decks', to='cards.deck'),
        ),
        migrations.AlterField(
            model_name='userdeck',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_decks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='correct_attempts',
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='known',
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='last_review_result',
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='review_history',
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='streak',
        ),
        migrations.RemoveField(
            model_name='usercardprogress',
            name='total_attempts',
        ),
    ]
