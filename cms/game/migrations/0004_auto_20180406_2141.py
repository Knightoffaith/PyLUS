# Generated by Django 2.0.3 on 2018-04-07 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_account_character'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='front_char',
            new_name='front_character',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='character_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='character_unapproved_name',
            new_name='unapproved_name',
        ),
        migrations.RemoveField(
            model_name='character',
            name='user',
        ),
        migrations.RemoveField(
            model_name='session',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='free_to_play',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='new_subscriber',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='session',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Session'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='address',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='objid',
            field=models.BigIntegerField(default=None),
            preserve_default=False,
        ),
    ]
