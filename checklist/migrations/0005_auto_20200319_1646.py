# Generated by Django 3.0.4 on 2020-03-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_questionnaire_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='total_score',
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]
