# Generated by Django 2.0.3 on 2018-04-11 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Enquiry', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]