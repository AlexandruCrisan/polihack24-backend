# Generated by Django 5.1.4 on 2024-12-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0003_alter_journey_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='rating',
            field=models.CharField(max_length=255, null=True),
        ),
    ]