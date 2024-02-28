# Generated by Django 4.1 on 2024-02-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viewset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('roll', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Generic',
        ),
    ]
