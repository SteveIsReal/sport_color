# Generated by Django 5.2.4 on 2025-07-08 08:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildboard', '0003_game_team'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2025, 7, 8, 8, 45, 10, 558804))),
                ('start_time', models.TimeField(default=datetime.datetime(2025, 7, 8, 8, 45, 10, 558826))),
                ('end_time', models.TimeField(default=datetime.datetime(2025, 7, 8, 8, 45, 10, 558838))),
            ],
        ),
        migrations.AlterField(
            model_name='score',
            name='tournament',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='buildboard.team'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='buildboard.team'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.event'),
        ),
    ]
