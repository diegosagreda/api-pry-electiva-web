# Generated by Django 4.1.7 on 2023-03-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApi', '0005_usuario_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paciente', models.CharField(max_length=100)),
                ('medicamento', models.CharField(max_length=100)),
                ('intensidad', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=100)),
            ],
        ),
    ]
