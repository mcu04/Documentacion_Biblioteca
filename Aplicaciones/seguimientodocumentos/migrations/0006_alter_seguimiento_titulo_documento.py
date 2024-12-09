# Generated by Django 5.1.3 on 2024-11-24 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimientodocumentos', '0005_rename_documentacion_seguimiento_titulo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='documentacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Seguimiento', to='seguimientodocumentos.documentacion'),
        ),
    ]
