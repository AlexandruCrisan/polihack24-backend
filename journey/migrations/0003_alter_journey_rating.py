# Generated by Django 5.1.4 on 2024-12-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0002_journey_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='rating',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]