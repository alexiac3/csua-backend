# Generated by Django 2.2.12 on 2020-07-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("db_data", "0019_auto_20200723_2121")]

    operations = [
        migrations.AlterField(
            model_name="officer",
            name="officer_since",
            field=models.DateField(blank=True, null=True),
        )
    ]
