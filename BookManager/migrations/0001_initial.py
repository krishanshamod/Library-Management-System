# Generated by Django 4.0.4 on 2022-05-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=100)),
                ('bookAuthor', models.CharField(max_length=100)),
            ],
        ),
    ]
