# Generated by Django 3.1.7 on 2022-10-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longURL', models.URLField(max_length=256)),
                ('shortURL', models.CharField(max_length=7)),
                ('createDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
