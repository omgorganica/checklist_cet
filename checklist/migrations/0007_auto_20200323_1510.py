# Generated by Django 3.0.4 on 2020-03-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_auto_20200319_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
