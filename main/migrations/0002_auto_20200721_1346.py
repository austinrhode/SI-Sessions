# Generated by Django 3.0.7 on 2020-07-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='image',
            field=models.ImageField(default='default.png', upload_to='session_images'),
        ),
    ]