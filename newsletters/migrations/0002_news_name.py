# Generated by Django 2.0.3 on 2018-04-11 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
