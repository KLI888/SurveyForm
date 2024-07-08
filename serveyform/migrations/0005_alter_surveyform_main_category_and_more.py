# Generated by Django 5.0.3 on 2024-06-21 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serveyform', '0004_surveyofficer_surver_officer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyform',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serveyform.maincategory'),
        ),
        migrations.AlterField(
            model_name='surveyform',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serveyform.subcategory'),
        ),
    ]
