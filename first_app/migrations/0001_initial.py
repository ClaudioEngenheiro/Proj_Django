# Generated by Django 4.2 on 2023-08-16 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paginas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(verbose_name='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.paginas')),
            ],
        ),
        migrations.AddField(
            model_name='paginas',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.topicos'),
        ),
    ]