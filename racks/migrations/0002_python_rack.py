# Generated by Django 3.2.5 on 2021-08-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='python_rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('explanation', models.CharField(max_length=10000)),
                ('tips_and_tricks', models.CharField(max_length=250)),
                ('code', models.TextField(null=True)),
            ],
        ),
    ]
