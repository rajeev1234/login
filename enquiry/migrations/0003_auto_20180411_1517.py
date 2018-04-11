# Generated by Django 2.0.3 on 2018-04-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_auto_20180411_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Enquiry_Subject',
            field=models.CharField(choices=[('FEATURE FILM PRODUCTION', 'FEATURE FILM PRODUCTION'), ('TVC/CORPORATES/AV’s', 'TVC/CORPORATES/AV’s'), ('FILMING/EVENT PERMISSIONS', 'FILMING/EVENT PERMISSIONS'), ('AUGMENTED REALITY CAMPAIGNS', 'AUGMENTED REALITY CAMPAIGNS'), ('3D DESIGNING/MODELING/WALKTHROUGHS/ANIMATIONS', '3D DESIGNING/MODELING/WALKTHROUGHS/ANIMATIONS'), ('IT CONSULTANCY', 'IT CONSULTANCY'), ('APPLICATION DEVELOPMENT/WEB DESIGNING', 'APPLICATION DEVELOPMENT/WEB DESIGNING'), ('MOBILE APPLICATION DEVELOPMENT', 'MOBILE APPLICATION DEVELOPMENT'), ('WEBCASTING SERVICES end to end', 'WEBCASTING SERVICES end to end'), ('CORPORATE IDENTITIES/BRAND BUILDING', 'CORPORATE IDENTITIES/BRAND BUILDING'), ('CREATIVE CONSULTANCY', 'CREATIVE CONSULTANCY'), ('PRINT DESIGNING', 'PRINT DESIGNING'), ('EVENTS', 'EVENTS')], max_length=100),
        ),
    ]
