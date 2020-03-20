# Generated by Django 2.1.11 on 2020-03-18 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence_database', '0002_auto_20200313_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='databaserequest',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='geneseekr',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='mlst',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='mlstcc',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='rmlst',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='sequencedata',
            name='rmlst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sequence_database.RMLST', verbose_name='rMLST Profile'),
        ),
        migrations.AlterField(
            model_name='serovar',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
        migrations.AlterField(
            model_name='vtyper',
            name='version',
            field=models.CharField(blank=True, max_length=48, null=True, verbose_name='pipeline_version'),
        ),
    ]