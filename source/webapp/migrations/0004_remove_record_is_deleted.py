# Generated by Django 4.1.6 on 2023-02-25 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_book_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='is_deleted',
        ),
    ]
