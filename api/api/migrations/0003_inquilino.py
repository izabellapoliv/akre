# Generated by Django 4.0.6 on 2022-08-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_proprietario_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquilino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('documento', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]