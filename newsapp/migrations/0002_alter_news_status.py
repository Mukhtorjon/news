# Generated by Django 3.2 on 2023-05-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('Qora', 'Qoralama'), ('Tay', 'Tayyor')], max_length=300),
        ),
    ]
