# Generated by Django 4.1.5 on 2023-08-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=2500)),
                ('date', models.DateField()),
                ('abstract', models.CharField(max_length=2500)),
                ('steps', models.JSONField()),
                ('pics', models.JSONField()),
                ('vids', models.JSONField()),
                ('conclusion', models.CharField(max_length=2500)),
            ],
        ),
    ]
