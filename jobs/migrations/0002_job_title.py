# Generated by Django 2.2.16 on 2020-10-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
