# Generated by Django 4.1.7 on 2023-03-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApi', '0008_recordatorio_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paciente', models.CharField(max_length=100)),
                ('medicamento', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
