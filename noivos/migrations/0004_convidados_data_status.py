# Generated by Django 5.1.2 on 2024-11-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0003_presentes_reservado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='convidados',
            name='data_status',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Resposta'),
        ),
    ]