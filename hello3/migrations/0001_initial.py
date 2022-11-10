# Generated by Django 4.0.6 on 2022-11-09 11:46

from django.db import migrations, models
import django.db.models.deletion
import hello3.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[hello3.models.alpha_only])),
                ('mail', models.EmailField(max_length=200)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello3.friend')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
