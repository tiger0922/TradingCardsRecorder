# Generated by Django 3.0 on 2020-05-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='album',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
