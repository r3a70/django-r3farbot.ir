# Generated by Django 4.0.4 on 2022-05-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_userfileinfo_chat_id_alter_userfileinfo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('chat_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('payeed', models.BooleanField()),
                ('idpay_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'pay_data',
            },
        ),
        migrations.CreateModel(
            name='UseMyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('status', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'use_my_account',
            },
        ),
    ]
