# Generated by Django 3.1.3 on 2020-11-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
