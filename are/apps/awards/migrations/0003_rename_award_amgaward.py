# Generated by Django 4.1 on 2022-09-05 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_award_org_person_mobile_award_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Award',
            new_name='AmgAward',
        ),
    ]
