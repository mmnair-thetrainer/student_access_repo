# Generated by Django 4.0.4 on 2022-05-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='images')),
            ],
            options={
                'db_table': 'facebook',
            },
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
    ]
