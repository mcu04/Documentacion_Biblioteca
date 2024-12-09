# Generated by Django 5.1.4 on 2024-12-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_archivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivo',
            options={'ordering': ['tipo']},
        ),
        migrations.AlterField(
            model_name='archivo',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Comunicacion', 'Comunicacion'), ('Comunidad', 'Comunidad'), ('Contable', 'Contable'), ('Gastos Comunes', 'Gastos Comunes'), ('Gestion de Emergencia', 'Gestion de Emergencia'), ('Inmobiliaria', 'Inmobiliaria'), ('Leyes Laborales', 'Leyes Laborales'), ('Libros', 'Libros'), ('Mantenimiento Preventivo', 'Mantenimiento Preventivo'), ('Planos', 'Planos'), ('Proveedores', 'Proveedores'), ('Reglamentos', 'Reglamentos'), ('Resolucion de Conflictos', 'Resolucion de Conflictos'), ('Temas de Seguridad', 'Temas de Seguridad'), ('Otros', 'Otros')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Administracion', 'Administracion'), ('Contabilidad', 'Contabilidad'), ('Legal', 'Legal'), ('Mantenimiento', 'Mantenimiento'), ('Personal', 'Personal'), ('Prevencion de Riesgos', 'Prevencion de Riesgos'), ('Seguridad', 'Seguridad'), ('Otros', 'Otros')], max_length=100, null=True),
        ),
    ]