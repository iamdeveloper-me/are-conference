# Generated by Django 4.1 on 2022-09-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='session',
            field=models.CharField(blank=True, choices=[('1', 'session-1'), ('2', 'session-2'), ('3', 'session-3'), ('4', 'session-4'), ('5', 'session-5'), ('6', 'session-6'), ('7', 'session-7'), ('8', 'session-8'), ('9', 'session-9'), ('10', 'session-10'), ('11', 'session-11'), ('12', 'session-12')], max_length=55, null=True),
        ),
    ]
