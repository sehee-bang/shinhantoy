# Generated by Django 4.1.5 on 2023-01-26 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': ('회원',), 'verbose_name_plural': '회원'},
        ),
        migrations.AlterModelTable(
            name='member',
            table='shinhan_member',
        ),
    ]
