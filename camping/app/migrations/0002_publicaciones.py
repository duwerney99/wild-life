# Generated by Django 3.2.9 on 2021-12-03 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_lugar', models.CharField(max_length=120)),
                ('ubicacion', models.CharField(max_length=250)),
                ('fotos', models.ImageField(upload_to='documents/wild-life-v1/app/static/images/')),
                ('videos', models.FileField(upload_to='documents/wild-life-v1/app/static/videos/')),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_publicacion', models.DateField(auto_now_add=True, verbose_name='Fecha de publicacion')),
                ('nombre_guia', models.CharField(max_length=120, verbose_name='Guia')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuarios')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]