# Generated by Django 4.1.7 on 2023-03-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApi', '0003_alter_solicitud_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(default='cliente', max_length=30),
        ),
    ]
