# Generated by Django 5.1.3 on 2024-11-24 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimientodocumentos', '0004_alter_seguimiento_existe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguimiento',
            old_name='documentacion',
            new_name='titulo_documento',
        ),
    ]