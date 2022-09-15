# Generated by Django 4.1 on 2022-09-12 11:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('work_status', models.CharField(blank=True, choices=[('Com', 'Completed:Application for work already done'), ('InPro', 'Inprogress:Application for work in progress or is planned in the immediate future')], max_length=50, null=True)),
                ('apply_type', models.CharField(blank=True, choices=[('Ind', 'Individual'), ('Org', 'Orgnization')], max_length=50, null=True)),
                ('nomination_type', models.CharField(blank=True, choices=[('S', 'Self'), ('O', 'Nomanating Other')], max_length=50, null=True)),
                ('full_name', models.CharField(blank=True, max_length=155, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('org_type', models.CharField(blank=True, max_length=155, null=True)),
                ('org_name', models.CharField(blank=True, max_length=155, null=True)),
                ('org_person_name', models.CharField(blank=True, max_length=155, null=True)),
                ('org_person_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('org_person_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('org_person_mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('org_address', models.CharField(blank=True, max_length=255, null=True)),
                ('org_web', models.URLField(blank=True, null=True)),
                ('work_exp', models.TextField(blank=True, null=True)),
                ('interpretetion', models.TextField(blank=True, null=True)),
                ('climate_change_challenge', models.TextField(blank=True, null=True)),
                ('award_category', models.CharField(blank=True, choices=[('a', 'Only awoid'), ('m', 'Only Minimize'), ('g', 'Only Generate'), ('a&m', 'Avoid and Minimize'), ('a,m&g', 'Avoid,Minimize and Generate')], max_length=50, null=True)),
                ('target_status', models.CharField(blank=True, max_length=155, null=True)),
                ('target_complated', models.TextField(blank=True, max_length=255, null=True)),
                ('ongoing_invitation_summary', models.TextField(blank=True, max_length=200, null=True)),
                ('invitation_summary', models.TextField(blank=True, max_length=200, null=True)),
                ('challenge_in_invitation', models.TextField(blank=True, max_length=200, null=True)),
                ('implement_invitation', models.TextField(blank=True, max_length=200, null=True)),
                ('amg_image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
