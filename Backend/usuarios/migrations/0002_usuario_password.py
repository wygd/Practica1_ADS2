# Generated by Django 2.2.4 on 2019-11-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='1234', max_length=40),
        ),
    ]
