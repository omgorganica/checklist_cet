# Generated by Django 3.0.4 on 2020-03-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_vehicletype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='total_score',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
