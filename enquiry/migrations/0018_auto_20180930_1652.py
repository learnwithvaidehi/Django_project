# Generated by Django 2.1.1 on 2018-09-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0017_auto_20180929_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='scheduled_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='scheduled_time',
            field=models.TimeField(blank=True),
        ),
    ]
