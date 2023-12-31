# Generated by Django 4.2.2 on 2023-07-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profail_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profail',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profail',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/user_photo/'),
        ),
    ]
