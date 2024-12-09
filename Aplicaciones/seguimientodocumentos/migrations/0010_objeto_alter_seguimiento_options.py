# Generated by Django 5.1.3 on 2024-12-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimientodocumentos', '0009_rename_titulo_documento_seguimiento_documentacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='seguimiento',
            options={'ordering': ['-fecha_actualizado'], 'verbose_name': 'Seguimiento', 'verbose_name_plural': 'Seguimientos'},
        ),
    ]