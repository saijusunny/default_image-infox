# Generated by Django 4.0.2 on 2022-03-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_productdetails_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image',
            field=models.ImageField(blank=True, default='icon.png', null=True, upload_to='image/'),
        ),
    ]