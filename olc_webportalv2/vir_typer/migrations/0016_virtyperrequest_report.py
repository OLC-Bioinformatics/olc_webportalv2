# Generated by Django 2.1.5 on 2019-08-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0015_auto_20190802_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtyperrequest',
            name='report',
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]
