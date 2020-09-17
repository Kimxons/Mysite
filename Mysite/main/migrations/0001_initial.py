# Generated by Django 3.1.1 on 2020-09-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('url', models.URLField(max_length=120)),
                ('tools', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('img_name', models.CharField(max_length=120)),
            ],
        ),
    ]