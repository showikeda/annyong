# Generated by Django 3.0.6 on 2020-06-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_article_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('message', models.TextField(max_length=1000, verbose_name='メッセージ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('created_by', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]