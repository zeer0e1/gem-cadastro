# Generated by Django 4.2.4 on 2023-08-23 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('localidade', models.CharField(max_length=200)),
                ('estado_civil', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=200)),
                ('operadora', models.CharField(max_length=20)),
                ('date_nascimento', models.DateField()),
                ('data_batismo', models.DateField(blank=True, null=True)),
                ('inicio_gem', models.DateField()),
                ('instrumento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.instrumento')),
            ],
        ),
    ]