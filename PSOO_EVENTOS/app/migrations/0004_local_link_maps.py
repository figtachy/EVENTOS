# Generated by Django 5.1.2 on 2024-10-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_evento_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='link_maps',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
