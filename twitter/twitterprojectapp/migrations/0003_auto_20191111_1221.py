# Generated by Django 2.2.7 on 2019-11-11 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterprojectapp', '0002_auto_20191111_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterprojectapp.User'),
        ),
    ]
