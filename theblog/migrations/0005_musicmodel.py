# Generated by Django 3.0.8 on 2020-08-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_onasmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.TextField()),
            ],
        ),
    ]
