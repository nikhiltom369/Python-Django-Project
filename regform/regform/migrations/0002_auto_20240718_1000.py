# Generated by Django 3.2.7 on 2024-07-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datas',
            old_name='username',
            new_name='email',
        ),
        migrations.AddField(
            model_name='datas',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datas',
            name='phone',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
