# Generated by Django 5.2.2 on 2025-07-03 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("buildboard", "0003_game_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buildboard.game",
                    ),
                ),
                (
                    "team1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buildboard.team",
                    ),
                ),
                (
                    "team2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buildboard.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_set", models.IntegerField(default=0)),
                ("score1", models.IntegerField(default=0)),
                ("score2", models.IntegerField(default=0)),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournament.tournament",
                    ),
                ),
            ],
        ),
    ]
