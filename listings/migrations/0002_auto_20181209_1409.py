# Generated by Django 2.1.3 on 2018-12-09 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_pulished',
            new_name='is_published',
        ),
    ]