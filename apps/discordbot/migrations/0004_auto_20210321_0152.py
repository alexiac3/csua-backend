# Generated by Django 2.2.19 on 2021-03-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("discordbot", "0003_auto_20210320_0343")]

    operations = [
        migrations.AlterField(
            model_name="connectfourgame",
            name="message_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="connectfourgame", name="player1", field=models.BigIntegerField()
        ),
        migrations.AlterField(
            model_name="connectfourgame", name="player2", field=models.BigIntegerField()
        ),
    ]
