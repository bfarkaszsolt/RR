# Generated by Django 2.0 on 2018-01-12 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_auto_20180113_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttomainpage',
            name='koncertcim',
            field=models.CharField(default='Best koncert ever', max_length=200),
            preserve_default=False,
        ),
    ]
