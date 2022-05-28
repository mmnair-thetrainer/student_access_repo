# Generated by Django 4.0.4 on 2022-04-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('bhp', models.CharField(max_length=100)),
                ('exshowroom', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
