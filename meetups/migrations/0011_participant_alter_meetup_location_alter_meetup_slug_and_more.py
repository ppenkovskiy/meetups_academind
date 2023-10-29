# Generated by Django 4.2.6 on 2023-10-29 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0010_rename_location_location_address_location_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
