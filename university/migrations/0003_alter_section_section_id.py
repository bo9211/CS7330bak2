# Generated by Django 5.0.4 on 2024-05-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_section_section_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_id',
            field=models.CharField(max_length=3),
        ),
    ]
