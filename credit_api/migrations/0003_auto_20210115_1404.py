# Generated by Django 3.0.5 on 2021-01-15 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit_api', '0002_auto_20210115_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit_detail',
            old_name='name',
            new_name='name_to',
        ),
        migrations.RemoveField(
            model_name='transaction_detail',
            name='name',
        ),
        migrations.RemoveField(
            model_name='transaction_detail',
            name='walletid',
        ),
        migrations.AddField(
            model_name='credit_detail',
            name='name_from',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction_detail',
            name='name_from',
            field=models.CharField(default='self', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction_detail',
            name='name_to',
            field=models.CharField(default='self', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction_detail',
            name='updated_balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction_detail',
            name='walletid_from',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='transaction_detail',
            name='walletid_to',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]