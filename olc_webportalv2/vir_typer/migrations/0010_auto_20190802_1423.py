# Generated by Django 2.1.5 on 2019-08-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0009_auto_20190730_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtyperproject',
            name='project_name',
            field=models.CharField(default='Required', max_length=256, unique=True),
        ),
    ]