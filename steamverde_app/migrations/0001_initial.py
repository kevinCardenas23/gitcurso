# Generated by Django 3.0.4 on 2020-04-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('sinopsis', models.TextField(max_length=2000, null=True)),
                ('anio', models.IntegerField()),
                ('actores', models.TextField(max_length=2000)),
                ('duracion', models.IntegerField()),
            ],
        ),
    ]