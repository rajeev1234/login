# Generated by Django 2.0.3 on 2018-04-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=50)),
                ('Service_Subcategory', models.CharField(max_length=100)),
                ('Service_Description', models.CharField(max_length=1000)),
                ('Service_Image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
