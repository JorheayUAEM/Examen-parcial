# Generated by Django 4.1 on 2022-09-29 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='genNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val1', models.IntegerField(blank=True, null=True)),
                ('val2', models.CharField(max_length=1024)),
                ('val3', models.IntegerField(blank=True, null=True)),
                ('val4', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]