# Generated by Django 2.1.7 on 2019-03-12 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='enroll_no',
            new_name='enrollment_no',
        ),
        migrations.RenameField(
            model_name='join',
            old_name='why_join',
            new_name='why_do_you_want_to_join_CIIE',
        ),
    ]