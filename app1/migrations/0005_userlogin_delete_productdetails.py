# Generated by Django 4.0.2 on 2022-03-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_productdetails_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.IntegerField()),
                ('repassword', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductDetails',
        ),
    ]
