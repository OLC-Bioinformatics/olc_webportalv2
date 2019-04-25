# Generated by Django 2.1.5 on 2019-04-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0007_metadatarequest_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='MLST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mlst', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='RMLST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmlst', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Serotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serotype', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=48)),
            ],
        ),
    ]
