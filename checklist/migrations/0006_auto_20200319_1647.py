# Generated by Django 3.0.4 on 2020-03-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_auto_20200319_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='total_score',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]