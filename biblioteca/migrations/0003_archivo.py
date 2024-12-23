# Generated by Django 5.1.4 on 2024-12-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_documento_estado_documento_fecha_descarga_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo_documento', models.CharField(max_length=255)),
                ('documento', models.FileField(upload_to='archivos/')),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
