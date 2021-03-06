# Generated by Django 2.1.5 on 2019-04-03 14:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0019_amrsummary_amr_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMRDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqid', models.CharField(default='', max_length=24)),
                ('amr_results', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
                ('amr_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amrdetail', to='geneseekr.AMRSummary')),
            ],
        ),
    ]
