# Generated by Django 4.0.2 on 2022-02-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Likes'),
        ),
    ]
