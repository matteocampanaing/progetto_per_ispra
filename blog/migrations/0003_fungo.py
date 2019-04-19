# Generated by Django 2.1.5 on 2019-04-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fungo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genere', models.DateField()),
                ('specie', models.CharField(max_length=200)),
                ('autore', models.CharField(max_length=200)),
                ('var_f', models.CharField(max_length=200)),
                ('autore_var', models.CharField(max_length=200)),
                ('data_verifica', models.CharField(max_length=200)),
                ('comune_provincia', models.CharField(max_length=200)),
                ('localita', models.CharField(max_length=200)),
                ('Altezza_slm', models.CharField(max_length=200)),
                ('principali_specie_vegetali', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=200)),
                ('tipologia_di_terreno', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('raccolto_da_legit', models.CharField(max_length=200)),
                ('determinato_da_determinavit', models.CharField(max_length=200)),
                ('indicazione_cartografica_igm', models.CharField(max_length=200)),
            ],
        ),
    ]