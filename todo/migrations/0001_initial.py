# Generated by Django 4.0.5 on 2022-06-26 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.executors')),
            ],
        ),
    ]
