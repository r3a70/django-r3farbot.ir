# Generated by Django 4.0.4 on 2022-05-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('plan_type', models.CharField(max_length=16)),
                ('buy_date', models.CharField(max_length=32)),
                ('expire_date', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
