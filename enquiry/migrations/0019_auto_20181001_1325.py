# Generated by Django 2.1.1 on 2018-10-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0018_auto_20180930_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='courses',
            field=models.ManyToManyField(related_name='enquries', to='enquiry.Course'),
        ),
    ]