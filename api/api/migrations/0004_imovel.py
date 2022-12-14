# Generated by Django 4.0.6 on 2022-08-01 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_inquilino'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25, unique=True)),
                ('endereco_cep', models.CharField(max_length=8)),
                ('endereco_rua', models.CharField(max_length=255)),
                ('endereco_numero', models.CharField(max_length=5)),
                ('endereco_bairro', models.CharField(max_length=255)),
                ('endereco_cidade', models.CharField(max_length=255)),
                ('endereco_uf', models.CharField(max_length=2)),
                ('endereco_complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_inquilino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inquilino')),
                ('fk_proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proprietario')),
            ],
        ),
    ]
