# Generated by Django 4.1.7 on 2023-02-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('paciente', models.CharField(max_length=100)),
                ('formula', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]
