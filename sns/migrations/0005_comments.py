# Generated by Django 3.0.6 on 2020-06-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0004_auto_20200617_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
    ]
