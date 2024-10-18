# Generated by Django 5.1 on 2024-10-15 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_apellido_user_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('userApoderado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Niño',
            fields=[
                ('userNiño', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('apoderadodelNiño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apoderado')),
            ],
        ),
        migrations.AddField(
            model_name='apoderado',
            name='niñodelApoderado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.niño'),
        ),
    ]
