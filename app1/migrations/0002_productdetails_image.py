# Generated by Django 4.0.2 on 2022-02-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
