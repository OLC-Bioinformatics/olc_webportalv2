# Generated by Django 2.1.5 on 2019-08-09 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0019_auto_20190809_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirTyperResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_results', to='vir_typer.VirTyperFiles')),
            ],
        ),
    ]
