# Generated by Django 3.2.9 on 2021-12-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensea',
            old_name='date',
            new_name='wdate',
        ),
        migrations.RemoveField(
            model_name='expensea',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='expensea',
            name='qty',
        ),
        migrations.AddField(
            model_name='expensea',
            name='pamount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expensea',
            name='pinterest',
            field=models.IntegerField(default=0),
        ),
    ]