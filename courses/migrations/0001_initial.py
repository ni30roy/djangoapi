# Generated by Django 5.0.7 on 2024-08-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lang', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
