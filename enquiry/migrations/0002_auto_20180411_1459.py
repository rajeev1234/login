# Generated by Django 2.0.3 on 2018-04-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='message',
            new_name='Enquiry_Message',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='subject',
            new_name='Enquiry_Subject',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='User',
            new_name='Enquiry_User',
        ),
    ]
