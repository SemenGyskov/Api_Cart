# Generated by Django 4.1.7 on 2023-03-05 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cost',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]