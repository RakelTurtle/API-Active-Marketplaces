# Generated by Django 4.1.2 on 2022-10-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Marketplace',
                'verbose_name_plural': 'Marketplaces',
            },
        ),
    ]