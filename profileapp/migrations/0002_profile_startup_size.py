# Generated by Django 3.2.7 on 2021-10-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='startup_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
