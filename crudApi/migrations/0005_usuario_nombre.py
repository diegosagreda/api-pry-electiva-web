# Generated by Django 4.1.7 on 2023-03-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApi', '0004_usuario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=200),
        ),
    ]
