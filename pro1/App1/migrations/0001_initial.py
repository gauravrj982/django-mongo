# Generated by Django 4.1.13 on 2024-01-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
