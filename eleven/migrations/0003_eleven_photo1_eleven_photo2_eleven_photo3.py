# Generated by Django 5.0.6 on 2024-06-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleven', '0002_banner_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleven',
            name='photo1',
            field=models.ImageField(null=True, upload_to='eleven1/'),
        ),
        migrations.AddField(
            model_name='eleven',
            name='photo2',
            field=models.ImageField(null=True, upload_to='eleven2/'),
        ),
        migrations.AddField(
            model_name='eleven',
            name='photo3',
            field=models.ImageField(null=True, upload_to='eleven3/'),
        ),
    ]
